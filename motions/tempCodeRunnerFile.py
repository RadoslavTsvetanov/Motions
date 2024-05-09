keyboard = Keyboard()

go_to_terminal = Motion(   
    Keys_trigger(trigger=[Key(KeyCode.from_char('y')), Key(KEYCODE.alt_l)]),
    Executor=Executor(sequence_to_execute=Sequence([Move_mouse_to_position(position=Position(611,955)),Click_on_mouse_position()]))

)

# click_motion = Motion(
#     Keys_trigger(trigger=[Key(KeyCode.from_char('a')),Key(KEYCODE.alt_l)]),
#     Executor=Executor(sequence_to_execute=Sequence([HotKey(['alt','tab']),HotKey(['alt','tab'])]))
# ) 

double_alt_tab = Motion(
    Keys_trigger(trigger=[Key(KeyCode.from_char('a')),Key(KEYCODE.down)]), 
    Executor=Executor(sequence_to_execute=Sequence([Hold_key('alt'),Key("tab"),Key("tab"),Release_key('alt')]))
)
def hold_alt():
    pyautogui.keyDown('alt')


print("hi2")
keyboard.add_to_listener(double_alt_tab)
keyboard.add_to_listener(go_to_terminal)
# keyboard.add_to_listener()
keyboard.set_up_keyboard_listener()
print("hi")
