from abc import ABC, abstractmethod
from typing import List
import pyautogui
from enum import Enum
class SEQUENCE_ITEM_TYPES(Enum):
    KEY = "key"
    SCROLL = "scroll"
    HOT_KEY = "hot_key"
    CLICK = "click"
    MOVE_MOUSE = "move_mouse"
    CUSTOM = "custom"

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Sequence_item(ABC):
    
    @abstractmethod
    def execute_key(self):
        pass

    @abstractmethod
    def get_value(self):
        pass



class Custom(Sequence_item):
    def __init__(self,callback):
        self.type = SEQUENCE_ITEM_TYPES.CUSTOM
        self.callback = callback

    def execute_key(self):
        self.callback()


    def get_value(self):
        return self.callback
class Key(Sequence_item):
    def __init__(self, key):
        self.type = SEQUENCE_ITEM_TYPES.KEY
        self.key = key 
        
    def execute_key(self):
        pyautogui.press(self.key)


    def get_value(self):
        return self.key

class HotKey(Sequence_item):
    def __init__(self, keys):
        self.keys = keys
        self.type = SEQUENCE_ITEM_TYPES.HOT_KEY
    def execute_key(self):
        pyautogui.hotkey(*self.keys)

    def get_value(self):
        return self.keys


class Scroll(Sequence_item):
    def __init__(self, scroll_type,value):
        self.scroll_type = scroll_type
        self.value = value
        self.type = SEQUENCE_ITEM_TYPES.SCROLL

    def execute_key(self):
        if self.scroll_type == "up":
            pyautogui.scroll(self.value)
        elif self.scroll_type == "down":
            pyautogui.scroll(self.value)

    def get_value(self):
        return self.value
    

class Click_on_mouse_position(Sequence_item): 
    def __init__(self):
        self.type = SEQUENCE_ITEM_TYPES.CLICK

    def execute_key(self):
        pyautogui.click()

    def get_value(self):
        return None

class Click_on_position(Sequence_item):
    def __init__(self,position: Position):
        self.type =  SEQUENCE_ITEM_TYPES.CLICK
        self.position = position
    def execute_key(self):
        pyautogui.moveTo(self.position.x, self.position.y)
        pyautogui.click()
    def get_value(self):
        return self.position


class Move_mouse_to_position(Sequence_item):
    def __init__(self, position: Position):
        self.position = position
        self.type = SEQUENCE_ITEM_TYPES.MOVE_MOUSE

    def execute_key(self):
        pyautogui.moveTo(self.position.x,self.position.y)

    def get_value(self):
        return self.position

class Hold_key(Sequence_item):
    def __init__(self,key):
        self.key = key
    
    def execute_key(self):
        print("key down")
        pyautogui.keyDown(self.key)

    def get_value(self):
        return self.key
    
class Release_key(Sequence_item):
    def __init__(self,key):
        self.key = key

    def execute_key(self):
        pyautogui.keyUp(self.key)


    def get_value(self):
        return self.key

class Sequence:
    def __init__(self, key_combination: List[Sequence_item]):
        self.key_combination = key_combination


combination_factories = dict()
combination_factories["hold"] = lambda x: Hold_key(x)
combination_factories["key"] = lambda x: Key(x)
combination_factories["scroll"] = lambda scroll_type, value: Scroll(scroll_type, value)
combination_factories["hot_key"] = lambda keys: HotKey(keys)
combination_factories["click_on_mouse_position"] = lambda: Click_on_mouse_position()
combination_factories["click_on_position"] = lambda position: Click_on_position(position)
combination_factories["move_mouse_to_position"] = lambda position: Move_mouse_to_position(position)
combination_factories["custom"] = lambda callback: Custom(callback)
