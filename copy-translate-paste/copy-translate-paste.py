import translators as ts
import pyautogui as pag
import pyperclip as ppc
from pynput import keyboard as kb

pag.FAILSAFE = False
esc_count = 0
text = ""

def on_press(key):
    global text
    if key == kb.Key.f7:        # Change Hotkey from 'F7' to whatever
        pag.hotkey('ctrl', 'c')
        text = ppc.paste()
        result = ts.google(text, from_language='en', to_language='th')
        if result != text:
            ppc.copy(result)
        else:
            ppc.copy(text)
        pag.hotkey('ctrl','v')    
        
def on_release(key):
    global esc_count
    if key == kb.Key.esc:
        esc_count += 1
    if esc_count >= 3:
        return False

with kb.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

listener = kb.Listener(on_press=on_press, on_release=on_release)

listener.start()