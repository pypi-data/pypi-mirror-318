from .api import ThreespaceSensor, ThreespaceCommand, StreamableCommands, ThreespaceCmdResult, threespaceGetHeaderLabels
from dataclasses import dataclass, field
import copy
from typing import Any, Callable
from enum import Enum

import numpy as np
import yostlabs.tss3.quaternion as yl_math

class ThreespaceStreamingStatus(Enum):
    Data = 0        #Normal data update
    DataEnd = 1     #This is the last packet being sent for this data update. This allows the user to more efficently handle their callback.
                    #For example, if you have an expensive computation that needs done over all the data, but only once per frame, it would
                    #be preferable to buffer the data received via the callback and only do the computation when DataEnd is received
    Paused = 2      #Streaming has been paused
    Resumed = 3     #Streaming has been resumed

    #Streaming manager is resetting. It is required that the callback unregisters everything is has registered
    #This option is intended for shutdown purposes or in complex applications where the user needs to completely
    #disable the streaming manager for some reason
    Reset = 4

from typing import NamedTuple
ThreespaceStreamingOption = NamedTuple("ThreespaceStreamingOption", [("cmd", StreamableCommands), ("param", int|None)])
class ThreespaceStreamingManager:
    """
    A class that manages multiple clients wanting streamed data. Will update the streaming
    slots and speed dynamically based on given requirements and allow those clients to
    access that data without having to worry about which streaming slot is being used by what data.
    """ 

    @dataclass
    class Command:
        cmd: StreamableCommands = None
        param: int = None

        slot: int = None
        registrations: set = field(default_factory=set, init=False)

        active: bool = False #If not active then it must have been queued for addition, so it will be set active immediately

        labels: str = None

    @dataclass
    class Callback:
        func: Callable[[ThreespaceStreamingStatus],None] = None
        hz: int = None

        only_newest: bool = False

        @property
        def interval(self):
            if self.hz is None: return None
            return 1000000 // self.hz

    def __init__(self, sensor: ThreespaceSensor):
        self.sensor = sensor

        self.num_slots = len(self.get_slots_from_sensor()) #This is just so if number of available slots ever changes, this changes to match it
        self.registered_commands: dict[tuple, ThreespaceStreamingManager.Command] = {}
        self.slots: list[ThreespaceStreamingManager.Command] = [] #The same as self.registered_commands, but allow indexing based on slot instead

        self.last_response: ThreespaceCmdResult|None = None
        self.results: dict[tuple,Any] = {}

        self.callbacks: dict[Callable, ThreespaceStreamingManager.Callback] = {}

        #Objects currently pausing the streaming
        self.pausers: set[object] = set()
        self.lockers: set[object] = set()

        #Keeps track of how many packets have been read. Useful for consumers to know if the values have been updated since they last read
        self.sample_count = 0

        self.enabled = False
        self.is_streaming = False #Store this seperately to attempt to allow using both the regular streaming and streaming manager via pausing and such

        #Set the initial streaming speed
        self.interval = int(self.sensor.get_settings("stream_interval"))    

        self.dirty = False
        self.validated = False

        #Control variable to manually control when updating happens here
        self.block_updates = False

        #Using interval instead of HZ because more precise and the result of ?stream_hz may not be exactly equal to what is set
        #However the functions for interfacing with these are still done in Hz
        self.max_interval = 0xFFFFFFFF
        self.min_interval = 1000000 / 2000

    @property
    def paused(self):
        return len(self.pausers) > 0
    
    @property
    def locked(self):
        return len(self.lockers) > 0    

    def pause(self, locker: object):
        if locker in self.pausers: return True
        if self.locked: return False
        self.pausers.add(locker)
        if len(self.pausers) == 1 and self.is_streaming:
            self.__stop_streaming()
            for callback in self.callbacks:
                callback(ThreespaceStreamingStatus.Paused)
        return True

    def resume(self, locker: object):
        try:
            self.pausers.remove(locker)
        except KeyError:
            return

        #Attempt to start again
        if len(self.pausers) == 0:
            for callback in self.callbacks:
                callback(ThreespaceStreamingStatus.Resumed)
            self.__apply_streaming_settings_and_update_state()

    def lock_modifications(self, locker: object):
        """
        This still allows the streaming manager to operate and register new objects. However, registration
        is limited to commands and speeds that are already operatable. Essentially, after this is called,
        it is not possible to do actions that require updating the sensors onboard settings/state. This gurantees
        streaming will not be stopped/restarted for time sensitive applications. 
        Note: This INCLUDES pausing/resuming, enabling/disabling...
        If you need to lock modifications, then pause or resume. The locker should unlock modifications, call the necessary function, and then lock again
        """
        self.lockers.add(locker)
    
    def unlock_modifications(self, locker: object):
        if not locker in self.lockers: return
        self.lockers.remove(locker)
        if not self.locked and self.dirty:
            self.__apply_streaming_settings_and_update_state()

    def reset(self):
        #Prevent the callbacks unregistrations from instantly taking effect regardless of if they pass immediate_update or not
        self.block_updates = True
        values = list(self.callbacks.values()) #To prevent concurrent dict modification, cache this
        for cb in values:
            cb.func(ThreespaceStreamingStatus.Reset)
        self.block_updates = False
        self.lockers.clear()
        self.pausers.clear()
        self.__apply_streaming_settings_and_update_state()
        if self.num_commands_registered != 0:
            raise RuntimeError(f"Failed to reset streaming manager. {self.num_commands_registered} commands still registered.\n {self.registered_commands}")
        if self.num_callbacks_registered != 0:
            raise RuntimeError(f"Failed to reset streaming manager. {self.num_callbacks_registered} callbacks still registered.\n {self.callbacks}")
        return True

    def update(self):
        if self.paused or not self.enabled or not self.sensor.is_streaming: return

        self.apply_updated_settings()
        self.sensor.updateStreaming()
        result = self.sensor.getOldestStreamingPacket()
        if result is not None:
            while result is not None:
                self.sample_count += 1
                self.last_response = result
                slot_index = 0
                for data in result.data:
                    while not self.slots[slot_index].active: slot_index += 1
                    cmd = self.slots[slot_index]
                    info = (cmd.cmd, cmd.param)
                    self.results[info] = data
                    slot_index += 1
                
                #Let all the callbacks know the data was updated
                for cb in self.callbacks.values():
                    if cb.only_newest: continue
                    cb.func(ThreespaceStreamingStatus.Data)

                result = self.sensor.getOldestStreamingPacket()
            
            for cb in self.callbacks.values():
                if cb.only_newest:
                    cb.func(ThreespaceStreamingStatus.Data)
                cb.func(ThreespaceStreamingStatus.DataEnd)

    def register_callback(self, callback: Callable[[ThreespaceStreamingStatus],None], hz=None, only_newest=False):
        if callback in self.callbacks: return
        self.callbacks[callback] = ThreespaceStreamingManager.Callback(callback, hz, only_newest)
        self.__update_streaming_speed()

    def unregister_callback(self, callback: Callable[[ThreespaceStreamingStatus],None]):
        if callback not in self.callbacks: return
        del self.callbacks[callback]
        self.__update_streaming_speed()

    def register_command(self, owner: object, command: StreamableCommands|ThreespaceStreamingOption, param=None, immediate_update=True):
        """
        Adds the given command to the streaming slots and starts streaming it

        Parameters
        ----
        owner : A reference to the object registering the command. A command is only unregistered after all its owners release it
        command : The command to register
        param : The parameter (if any) required for the command to be streamed. The command and param together identify a single slot
        immediate_update : If true, the streaming manager will immediately change the streaming slots on the sensor. If doing bulk registers, it
        is useful to set this as False until the last one for performance purposes.

        Returns
        -------
        True : Successfully registered the command
        False : Failed to register the command. Streaming slots are full
        """
        if isinstance(command, tuple):
            param = command[1]
            command = command[0]
        info = (command, param)
        if info in self.registered_commands: #Already registered, just add this as an owner
            cmd = self.registered_commands[info]
            if len(cmd.registrations) == 0 and self.num_commands_registered >= self.num_slots: #No room to register
                return False
            
            cmd.registrations.add(owner)
            if immediate_update and self.dirty:
                return self.__apply_streaming_settings_and_update_state()
            return True
        
        if self.locked: #Wasn't already registered, so don't allow new registrations
            return False
        
        #Make sure to only consider a command registered if it has registrations
        num_commands_registered = self.num_commands_registered
        if num_commands_registered >= self.num_slots: #No room to register
            return False
        
        #Register the command and add it to the streaming
        self.registered_commands[info] = ThreespaceStreamingManager.Command(command, param=param, slot=num_commands_registered)
        self.registered_commands[info].labels = self.sensor.getStreamingLabel(command.value).data
        self.registered_commands[info].registrations.add(owner)
        self.dirty = True
        if immediate_update:
            return self.__apply_streaming_settings_and_update_state()
        return True

    def unregister_command(self, owner: object, command: StreamableCommands|ThreespaceStreamingOption, param=None, immediate_update=True):
        """
        Removes the given command to the streaming slots and starts streaming it

        Parameters
        ----------
        owner : A reference to the object unregistering the command. A command is only unregistered after all its owners release it
        command : The command to unregister
        param : The param (if any) required for the command
        immediate_update : If true, the streaming manager will immediately change the streaming slots on the sensor. If doing bulk unregisters, it
        is useful to set this as False until the last one for performance purposes.
        """
        if isinstance(command, tuple):
            param = command[1]
            command = command[0]
        info = (command, param)
        if info not in self.registered_commands:
            return
        
        try:
            self.registered_commands[info].registrations.remove(owner)
        except KeyError:
            return #This owner wasn't registered to begin with, just ignore
        
        #Nothing else to do
        if len(self.registered_commands[info].registrations) != 0: 
            return
        
        #Remove the command from streaming since nothing owns it anymore
        self.dirty = True
        if immediate_update:
            self.__apply_streaming_settings_and_update_state()


    def __build_stream_slots_string(self):
        cmd_strings = []
        self.slots.clear()
        if self.num_commands_registered == 0: return "255"
        i = 0
        for cmd_key in self.registered_commands:
            cmd = self.registered_commands[cmd_key]
            if not cmd.active: continue #Skip non active registrations
            self.slots.append(cmd)
            cmd.slot = i
            if cmd.param == None:
                cmd_strings.append(str(cmd.cmd.value))
            else:
                cmd_strings.append(f"{cmd.cmd.value}:{cmd.param}")
            i += 1
        return ','.join(cmd_strings)

    #More user friendly version of __apply_streaming_settings_and_update_state that prevents the user from calling it when not needed.
    def apply_updated_settings(self):
        """
        This applys the current settings of the streaming manager and updates its state. This is normally done automatically, however
        if the user is registering/unregistering with immediate_update turned off, this can be called to force the update.
        """
        if not self.dirty: return self.validated
        return self.__apply_streaming_settings_and_update_state()

    def __apply_streaming_settings_and_update_state(self, ignore_lock=False):
        """
        Used to apply the current configuration this manager represents to the streaming.
        This involves disabling streaming if currently running
        """
        if self.block_updates or (self.locked and not ignore_lock):
            return False
        
        if self.sensor.is_streaming:
            self.__stop_streaming()
        
        #Clean up any registrations that need removed and activate any that need activated
        if self.dirty:
            to_remove = []
            for k, v in self.registered_commands.items():
                if len(v.registrations) == 0:
                    to_remove.append(k)
                    continue
                v.active = True
            for key in to_remove:
                del self.registered_commands[key]
                if key in self.results:
                    del self.results[key]
        self.dirty = False

        if self.num_commands_registered > 0:
            slots_string = self.__build_stream_slots_string()
            err, num_successes = self.sensor.set_settings(stream_slots=slots_string, stream_interval=self.interval)
            if err:
                self.validated = False
                return False
            if not self.paused and self.enabled: 
                self.__start_streaming() #Re-enable
        
        self.validated = True
        return True

    def __update_streaming_speed(self):        
        required_interval = None
        for callback in self.callbacks.values():
            if callback.interval is None: continue
            if required_interval is None or callback.interval < required_interval:
                required_interval = callback.interval

        if required_interval is None: #Treat required as current to make sure the current interval is still valid
            required_interval = self.interval 

        required_interval = min(self.max_interval, max(self.min_interval, required_interval))
        if required_interval != self.interval:
            print(f"Updating streaming speed from {1000000 / self.interval}hz to {1000000 / required_interval}hz")
            self.interval = int(required_interval)
            self.dirty = True
            self.__apply_streaming_settings_and_update_state()

    def __start_streaming(self):
        self.sensor.startStreaming()
        self.is_streaming = True

    def __stop_streaming(self):
        self.sensor.stopStreaming()
        self.is_streaming = False

    @property
    def num_commands_registered(self):
        return len([v for v in self.registered_commands.values() if len(v.registrations) != 0])
    
    @property
    def num_callbacks_registered(self):
        return len(self.callbacks)

    def get_value(self, command: StreamableCommands|ThreespaceStreamingOption, param=None):
        if isinstance(command, tuple):
            param = command[1]
            command = command[0]
        return self.results.get((command, param), None)

    def get_last_response(self):
        return self.last_response

    def get_header(self):
        return self.last_response.header  

    def get_cmd_labels(self):
        return ','.join(cmd.labels for cmd in self.registered_commands.values())
    
    def get_header_labels(self):
        order = threespaceGetHeaderLabels(self.sensor.header_info)
        return ','.join(order)
    
    def get_response_labels(self):
        return ','.join([self.get_header_labels(), self.get_cmd_labels()])

    def enable(self):
        if self.enabled:
            return
        self.enabled = True
        self.__apply_streaming_settings_and_update_state()

    def disable(self):
        if not self.enabled:
            return
        if self.is_streaming:
            self.__stop_streaming()
        self.enabled = False

    def set_max_hz(self, hz: float):
        if hz <= 0 or hz > 2000: 
            raise ValueError(f"Invalid streaming Hz {hz}")
        self.min_interval = 1000000 // hz
        self.__update_streaming_speed()

    def set_min_hz(self, hz: float):
        if hz <= 0 or hz > 2000: 
            raise ValueError(f"Invalid streaming Hz {hz}")
        self.max_interval = 1000000 // hz
        self.__update_streaming_speed()

    def get_slots_from_sensor(self):
        """
        get a list containing the streaming information from the current sensor
        """
        slot_setting: str = self.sensor.get_settings("stream_slots")
        slots = slot_setting.split(',')
        slot_info = []
        for slot in slots:
            info = slot.split(':')
            slot = int(info[0]) #Ignore parameters if any
            param = None
            if len(info) > 1:
                param = int(info[1])
            if slot != 255:
                slot_info.append((slot, param))
            else:
                slot_info.append(None)
        
        return slot_info

class ThreespaceGradientDescentCalibration:

    @dataclass
    class StageInfo:
        start_vector: int
        end_vector: int
        stage: int
        scale: float

        count: int = 0

    MAX_SCALE = 1000000000
    MIN_SCALE = 1
    STAGES = [
        StageInfo(0, 6, 0, MAX_SCALE),
        StageInfo(0, 12, 1, MAX_SCALE),
        StageInfo(0, 24, 2, MAX_SCALE)
    ]

    #Note that each entry has a positive and negative vector included in this list
    CHANGE_VECTORS = [
        np.array([0,0,0,0,0,0,0,0,0,.0001,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,0,0,-.0001,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,0,0,0,.0001,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,0,0,0,-.0001,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,0,0,0,0,.0001], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,0,0,0,0,-.0001], dtype=np.float64), #First 6 only try to change the bias
        np.array([.001,0,0,0,0,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([-.001,0,0,0,0,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,.001,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,-.001,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,0,.001,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,0,-.001,0,0,0], dtype=np.float64), #Next 6 only try to change the scale
        np.array([0,.0001,0,0,0,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,-.0001,0,0,0,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,.0001,0,0,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,-.0001,0,0,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,.0001,0,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,-.0001,0,0,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,.0001,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,-.0001,0,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,.0001,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,-.0001,0,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,.0001,0,0,0,0], dtype=np.float64),
        np.array([0,0,0,0,0,0,0,-.0001,0,0,0,0], dtype=np.float64), #Next 12 only try to change the shear
    ]

    def __init__(self, relative_sensor_orients: list[np.ndarray[float]], no_inverse=False):
        """
        Params
        ------
        relative_sensor_orients : The orientation of the sensor during which each sample is taken if it was tared as if pointing into the screen. 
        The inverse of these will be used to calculate where the axes should be located relative to the sensor
        no_inverse : The relative_sensor_orients will be treated as the sample_rotations
        """
        if no_inverse:
            self.rotation_quats = relative_sensor_orients
        else:
            self.rotation_quats = [np.array(yl_math.quat_inverse(orient)) for orient in relative_sensor_orients]

    def apply_parameters(self, sample: np.ndarray[float], params: np.ndarray[float]):
        bias = params[9:]
        scale = params[:9]
        scale = scale.reshape((3, 3))
        return scale @ (sample + bias)

    def rate_parameters(self, params: np.ndarray[float], samples: list[np.ndarray[float]], targets: list[np.ndarray[float]]):
        total_error = 0
        for i in range(len(samples)):
            sample = samples[i]
            target = targets[i]

            sample = self.apply_parameters(sample, params)
            
            error = target - sample
            total_error += yl_math.vec_len(error)
        return total_error

    def generate_target_list(self, origin: np.ndarray):
        targets = []
        for orient in self.rotation_quats:
            new_vec = np.array(yl_math.quat_rotate_vec(orient, origin), dtype=np.float64)
            targets.append(new_vec)
        return targets

    def __get_stage(self, stage_number: int):
        if stage_number >= len(self.STAGES):
            return None
        #Always get a shallow copy of the stage so can modify without removing the initial values
        return copy.copy(self.STAGES[stage_number])

    def calculate(self, samples: list[np.ndarray[float]], origin: np.ndarray[float], verbose=False, max_cycles_per_stage=1000):
        targets = self.generate_target_list(origin)
        initial_params = np.array([1,0,0,0,1,0,0,0,1,0,0,0], dtype=np.float64)
        stage = self.__get_stage(0)

        best_params = initial_params
        best_rating = self.rate_parameters(best_params, samples, targets)
        count = 0
        while True:
            last_best_rating = best_rating
            params = best_params

            #Apply all the changes to see if any improve the result
            for change_index in range(stage.start_vector, stage.end_vector):
                change_vector = self.CHANGE_VECTORS[change_index]
                new_params = params + (change_vector * stage.scale)
                rating = self.rate_parameters(new_params, samples, targets)

                #A better rating, store it
                if rating < best_rating:
                    best_params = new_params
                    best_rating = rating
            
            if verbose and count % 100 == 0:
                print(f"Round {count}: {best_rating=} {stage=}")
            
            #Decide if need to go to the next stage or not
            count += 1
            stage.count += 1
            if stage.count >= max_cycles_per_stage:
                stage = self.__get_stage(stage.stage + 1)
                if stage is None:
                    if verbose: print("Done from reaching count limit")
                    break
                if verbose: print("Going to next stage from count limit")
                
            if best_rating == last_best_rating: #The rating did not improve
                if stage.scale == self.MIN_SCALE: #Go to the next stage since can't get any better in this stage!
                    stage = self.__get_stage(stage.stage + 1)
                    if stage is None:
                        if verbose: print("Done from exhaustion")
                        break
                    if verbose: print("Going to next stage from exhaustion")
                else:   #Reduce the size of the changes to hopefully get more accurate tuning
                    stage.scale *= 0.1  
                    if stage.scale < self.MIN_SCALE:
                        stage.scale = self.MIN_SCALE
            else: #Rating got better! To help avoid falling in a local minimum, increase the size of the change to see if that could make it better
                stage.scale *= 1.1
        
        if verbose:
            print(f"Final Rating: {best_rating}")
            print(f"Final Params: {best_params}")

        return best_params

from xml.dom import minidom, Node
class ThreespaceFirmwareUploader:

    def __init__(self, sensor: ThreespaceSensor, file_path: str = None, percentage_callback: Callable[[int],None] = None, verbose: bool = False):
        self.sensor = sensor
        self.set_firmware_path(file_path)
        self.verbose = verbose

        self.percent_complete = 0
        self.callback = percentage_callback

    def set_firmware_path(self, file_path: str):
        if file_path is None: 
            self.firmware = None
            return
        self.firmware = minidom.parse(file_path)

    def set_percent_callback(self, callback: Callable[[float],None]):
        self.callback = callback

    def set_verbose(self, verbose: bool):
        self.verbose = verbose

    def get_percent_done(self):
        return self.percent_complete
    
    def __set_percent_complete(self, percent: float):
        self.percent_complete = percent
        if self.callback:
            self.callback(percent)

    def log(self, *args):
        if not self.verbose: return
        print(*args)

    def upload_firmware(self):
        self.percent_complete = 0
        if not self.sensor.in_bootloader:
            self.sensor.enterBootloader()
        self.__set_percent_complete(5)
        
        boot_info = self.sensor.bootloader_get_info()

        root = self.firmware.firstChild
        for c in root.childNodes:
            if c.nodeType == Node.ELEMENT_NODE:
                name = c.nodeName
                if name == "SetAddr":
                    self.log("Write S")
                    error = self.sensor.bootloader_erase_firmware()
                    if error:
                        self.log("Failed to erase firmware:", error)
                    else:
                        self.log("Successfully erased firmware")
                    self.__set_percent_complete(20)
                elif name == "MemProgC":
                    mem = bytes.fromhex(c.firstChild.nodeValue)
                    self.log("Attempting to program", len(mem), "bytes to the chip")
                    cpos = 0
                    while cpos < len(mem):
                        memchunk = mem[cpos : min(len(mem), cpos + boot_info.pagesize)]
                        error = self.sensor.bootloader_prog_mem(memchunk)
                        if error:
                            self.log("Failed upload:", error)
                        else:
                            self.log("Wrote", len(memchunk), "bytes successfully to offset", cpos)
                        cpos += len(memchunk)
                        self.__set_percent_complete(20 + cpos / len(mem) * 79)
                elif name == "Run":
                    self.log("Resetting with new firmware.")
                    self.sensor.bootloader_boot_firmware()
                    self.__set_percent_complete(100)

if __name__ == "__main__":
    firmware_file = "D:\\svn\\trunk\\3Space\\TSS_3.0_Firmware\\Nuvoton_BASE_Project\\build\\Application.xml"
    sensor = ThreespaceSensor()
    sensor.set_settings(debug_level=0)
    sensor.set_settings(cpu_speed=192000000, power_initial_hold_state=0)
    sensor.commitSettings()

    firmware_uploader = ThreespaceFirmwareUploader(firmware_file, verbose=True)
    firmware_uploader.upload_firmware(sensor)

    print(sensor.get_settings("version_firmware"))

