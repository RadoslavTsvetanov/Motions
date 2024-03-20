from input_devices import Keyboard
from trigger import Keys_trigger
from combination import Key
import threading
from pynput.keyboard import KeyCode,Key as KEYCODE
# keyboard = Keyboard()
# alt_r_trigger = Keys_trigger([Key('a'), Key('b')],Keyboard_singleton=None)



keyboard = Keyboard()
a_b_trigger = Keys_trigger(trigger=[Key(KeyCode.from_char('a')),Key(KEYCODE.alt_gr)],Keyboard_singleton=None)

keyboard.triggers_to_watch_for.append(a_b_trigger)
keyboard.set_up_keyboard_listener()