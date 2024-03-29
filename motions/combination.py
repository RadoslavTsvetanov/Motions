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
    

class Click_on_mouse_position(Sequence_item): #TODO in the future to make it so that in inherets or implemnts a base click class and this just clicks on the mouse pos coordinates, the additional functionality before clicking might be done by passing a calback which excutes before click
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

    
class Sequence:
    def __init__(self, key_combination: List[Sequence_item]):
        self.key_combination = key_combination


move_mouse = Move_mouse_to_position(Position(100,100))
move_mouse.execute_key()