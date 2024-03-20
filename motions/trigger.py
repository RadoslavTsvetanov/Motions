from abc import ABC, abstractmethod
from combination import Key
from typing import List
from input_devices import Keyboard
import threading
import time

class Trigger(ABC):
    def __init__(self, trigger):
        pass
    
    @abstractmethod
    def listen_for_trigger(self):
        pass

class Keys_trigger(Trigger):
    def __init__(self, trigger: List[Key], Keyboard_singleton: Keyboard=None):
        super().__init__(trigger)
        self.trigger = trigger
        self.keyboard = Keyboard_singleton

    def check_trigger(self,current_keys=None):
        if self.keyboard == None :
            keys_to_listen_for = set({trigger.get_value() for trigger in self.trigger})  # Using set comprehension
            print(keys_to_listen_for,self.keyboard.keys_pressed,keys_to_listen_for.issubset(self.keyboard.keys_pressed))
            return keys_to_listen_for.issubset(self.keyboard.keys_pressed)
    
        else:
            keys_to_listen_for = set({trigger.get_value() for trigger in self.trigger})
            print("listenimg keys",keys_to_listen_for)
            print("current keys",current_keys)
            return keys_to_listen_for.issubset(self.keyboard.keys_pressed)
            
        
    def listen_for_trigger(self): 
        while True:
            if self.check_trigger():
                print("Trigger detected")
            time.sleep(1)

#---------------------------------------------------
# KEYBOARD = Keyboard()
# # keyboard_thread = threading.Thread(target=KEYBOARD.set_up_keyboard_listener)
# # keyboard_thread.start()
# #? it does not work with multiprocessing. Possible fix is to use copies instead of references
# # Simulating the pressed keys for testing
# a_b_trigger = Keys_trigger(trigger=[Key("a"),Key("b")], Keyboard_singleton=KEYBOARD)
# print(KEYBOARD.keys_pressed)
# print(a_b_trigger.listen_for_trigger())