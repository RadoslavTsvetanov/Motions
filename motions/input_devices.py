from typing import List
from pynput.keyboard import Key, Listener
import threading
import time
import pyautogui

def keyboard_pressed_keys_callback(keys: List[Key],callback):
    callback(keys)


class Keyboard: # ctrl + c is not detected in a good way
    def __init__(self):
        self.keys_pressed = set() 

    def on_press(self, key: Key):
        self.keys_pressed.add(key)  
        return key

    def on_release(self, key: Key):
        self.keys_pressed.discard(key) 
        if key == Key.esc:
            return False

    def view_pressed_keys(self):
        print(self.keys_pressed)

    def set_up_keyboard_listener(self):
        thread = threading.Thread(target=self.view_pressed_keys)
        thread.start()
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
        thread.join()

    








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
