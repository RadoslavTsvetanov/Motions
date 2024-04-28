from typing import List
from pynput.keyboard import Key, Listener
import threading
import time
import pyautogui
from motion import Motions

class Keyboard: # ctrl + c is not detected in a good way
    def __init__(self):
        self.keys_pressed = set() 
        self.motions: Motions = Motions()
    def on_press(self, key: Key):
        if key in self.keys_pressed:
            return

        self.keys_pressed.add(key)
        check_thread = threading.Thread(target=self.motions.check_motions, args=(self.keys_pressed,))
        check_thread.start()
        return key


    def on_release(self, key: Key):
        self.keys_pressed.discard(key)
        if key == Key.esc:
            return False

    def view_pressed_keys(self):
        print(self.keys_pressed)

    def set_up_keyboard_listener(self):
        
        
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def add_to_listener(self, Motion):
        self.motions.add_motion(Motion)

    def clear_keys(self): 
        self.keys_pressed = []


# class InputListener:
#     def __init__(self,Keyboard: Keyboard) -> None:
#         self.keyboard = Keyboard


#     def 

# class KIeyboardState:
#     def __init__(self):
#         self.state = []

# # Usage
# keyboard = Keyboard()
# keyboard.set_up_keyboard_listener()
