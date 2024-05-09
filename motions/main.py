from input_devices import Keyboard
from combination import Sequence,Key,HotKey,Scroll,Move_mouse_to_position,Click_on_mouse_position,Position,Custom,Hold_key,Release_key
import executor
from trigger import Keys_trigger
from combination import Key
from motion import Motion, Motions
from executor import Executor,ExeExecutor
import threading
import time
from pynput.keyboard import KeyCode,Key as KEYCODE
import pyautogui
from server import udp_server,MyHandler

new_motion = Motion(Trigger=None,Executor=ExeExecutor("node motions/index.js"))
new_motion.execute()


example_handler = MyHandler([new_motion])


udp_server(example_handler)
























# keyboard = Keyboard()
# # alt_r_trigger = Keys_trigger([Key('a'), Key('b')],Keyboard_singleton=None)

# # since most special keys already do something a good key to use is the alt_ge + the alt_gr version of the key a -> á   





# keyboard = Keyboard()

# go_to_terminal = Motion(   
#     Keys_trigger(trigger=[Key(KeyCode.from_char('y')), Key(KEYCODE.alt_l)]),
#     Executor=Executor(sequence_to_execute=Sequence([Move_mouse_to_position(position=Position(611,955)),Click_on_mouse_position()]))

# )

# # click_motion = Motion(
# #     Keys_trigger(trigger=[Key(KeyCode.from_char('a')),Key(KEYCODE.alt_l)]),
# #     Executor=Executor(sequence_to_execute=Sequence([HotKey(['alt','tab']),HotKey(['alt','tab'])]))
# # ) 

# double_alt_tab = Motion(
#     Keys_trigger(trigger=[Key(KeyCode.from_char('a')),Key(KEYCODE.down)]), 
#     Executor=Executor(sequence_to_execute=Sequence([Hold_key('alt'),Key("tab"),Key("tab"),Release_key('alt')]))
# )
# def hold_alt():
#     pyautogui.keyDown('alt')


# print("hi2")
# keyboard.add_to_listener(double_alt_tab)
# keyboard.add_to_listener(go_to_terminal)
# # keyboard.add_to_listener()
# keyboard.set_up_keyboard_listener()
# print("hi")

# motions = Motions()



