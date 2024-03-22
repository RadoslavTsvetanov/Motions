from input_devices import Keyboard
from combination import Sequence,Key,HotKey,Scroll,Move_mouse_to_position,Click_on_mouse_position,Position,Custom
import executor
from trigger import Keys_trigger
from combination import Key
from motion import Motion
from executor import Executor
import threading
import time
from pynput.keyboard import KeyCode,Key as KEYCODE
import pyautogui
# keyboard = Keyboard()
# alt_r_trigger = Keys_trigger([Key('a'), Key('b')],Keyboard_singleton=None)

# since most special keys already do something a good key to use is the alt_ge + the alt_gr version of the key a -> á   

keyboard = Keyboard()


click_motion = Motion(
    Keys_trigger(trigger=[Key(KeyCode.from_char('á')),Key(KEYCODE.alt_gr)]),
    Executor=Executor(sequence_to_execute=Sequence([Move_mouse_to_position(Position(200,200))]))
    )

print("hi2")
keyboard.add_to_listener(click_motion)
keyboard.set_up_keyboard_listener()
print("hi")