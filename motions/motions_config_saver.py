import json
from motion import Motion
import trigger as triggerTrigger
import executor as executorExecutor
from combination import Key
from combination import Sequence,Key,HotKey,Scroll,Move_mouse_to_position,Click_on_mouse_position,Position,Custom,Hold_key,Release_key
from enum import Enum
from pynput.keyboard import KeyCode,Key as KEYCODE
from custom_keys import custom_keys

def get_value_from_dict_without_possible_exception(dict,key):
    try:
        return  dict[key]    
    except Exception:
        return None
""" 

{
    type
    executor:{
        type: string,
        data:  
    }
}



"""
class ENTITIES_TYPES(Enum):
    WEB=1,
    SCREEN=2,
    KEYBAORD=3,
    CUSTOM=4,
    WEB_TO_COMMAND=5


class Entity:
    entity_type: ENTITIES_TYPES
    data: object


class motion_type_for_config:
    motion_type: ENTITIES_TYPES # name is a bit stupid since just type is a reserved word
    executor: Entity
    trigger: Entity



def motion_factory(motion_data: motion_type_for_config) -> Motion | None:  
    print(motion_data)
    #!--- for now implemenatation for just keys trigger with key executor
    try:
        trigger_arr = []
        for trigger in motion_data["trigger"]["data"]:
            new_key = get_value_from_dict_without_possible_exception(custom_keys,trigger)
            print(new_key)
            if new_key is None:
                new_key =  KeyCode.from_char(trigger)
                trigger_arr.append(Key(new_key))
            else:
                trigger_arr.append(Key(new_key))
        
        new_trigger = triggerTrigger.Keys_trigger(trigger=trigger_arr)
        new_executor = executorExecutor.Executor(sequence_to_execute=Sequence([]))
        return Motion(Trigger=new_trigger,Executor=new_executor)
    except Exception as e:
        print(e)
        return None
    



    
def format_motion_data_to_motion_json(motion_data):
    return {
        "trigger": motion_data.trigger,
    }


class Config:
    def __init__(self,path_to_config):
        self.path_to_config = path_to_config

    def load_config(self):
        with open(self.path_to_config, "r") as file:
            data = json.load(file)
            return data


    def construct_motions_from_config(self):
        data = self.load_config()
        motions = []
        for motion_config in data.motions:
            new_motion = motion_factory(motion_data=motion_config)

            if new_motion is not None:
                motions.append(new_motion)
        return motions


    def add_motion(self,motion_info):
        config = self.load_config()
        config.motions.append(format_motion_data_to_motion_json(motion_info))
        with open(self.path_to_motion, "w") as file:
            file.write(json.dump(config))
        
        pass


config = Config("./config.json")





new_motion = motion_factory({
    "motion_type":1,
    "executor":{
        "type":1,
        "data":"" 
    },
    "trigger":{
        "type":1,
        "data":["down","a"]
    }
})


new_motion.Trigger.debug()