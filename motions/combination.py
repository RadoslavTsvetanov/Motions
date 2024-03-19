from abc import ABC, abstractmethod
from typing import List
import pyautogui
from enum import Enum
class SEQUENCE_ITEM_TYPES(Enum):
    KEY = "key"
    SCROLL = "scroll"
    HOT_KEY = "hot_key"


class Sequence_item(ABC):
    
    @abstractmethod
    def execute_key(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

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

class Sequence:
    def __init__(self, key_combination: List[Sequence_item]):
        self.key_combination = key_combination
