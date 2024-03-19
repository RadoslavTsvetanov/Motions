from input_devices import Keyboard
from trigger import Keys_trigger
from combination import Key
import threading
# keyboard = Keyboard()
# alt_r_trigger = Keys_trigger([Key('a'), Key('b')],Keyboard_singleton=None)



keyboard = Keyboard()
a_b_trigger = Keys_trigger(trigger=[Key("a"),Key( "b")],Keyboard_singleton=keyboard)
keyboard.triggers_to_watch_for.append(a_b_trigger)
keyboard_thread = threading.Thread(target=keyboard.set_up_keyboard_listener)
keyboard_thread.start()



