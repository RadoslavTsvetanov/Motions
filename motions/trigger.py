from abc import ABC, abstractmethod
from combination import Key
from typing import List
from input_devices import Keyboard
import threading
import time

def check_keys_appear(set1, set2): #!!!!!!!! stupid python set of types current keys does not provide the actual value but the string value -> 'a' and not a   (the representation is "'s'" and not "s")
    print("checking",set1,set2)
    for i in set2:
        print("i",i)
    
    for element in set1:
        #print(element[1::(len(element) -)])
        if element not in set2:
            return False
    return True


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
            # formatted_current_keys = set()
            # for element in current_keys:
            #     formatted_current_keys.add(element.char)
            return keys_to_listen_for.issubset(current_keys)
        
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