from input_devices import Keyboard
from trigger import Keys_trigger
from combination import Key
import threading
# keyboard = Keyboard()
# alt_r_trigger = Keys_trigger([Key('a'), Key('b')],Keyboard_singleton=None)



keyboard = Keyboard()
a_b_trigger = Keys_trigger(trigger=[Key("b"),Key( "a")],Keyboard_singleton=None)
keyboard.triggers_to_watch_for.append(a_b_trigger)
keyboard.keys_pressed.add('a')
keyboard.keys_pressed.add('b')
keyboard.set_up_keyboard_listener()