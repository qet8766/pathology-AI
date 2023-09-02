from pynput import keyboard
import win32api
import clipboard
from time import sleep
import pyautogui

pyautogui.FAILSAFE = False
def on_activate_h():
    win32api.WinExec("calc.exe")
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<esc>')
    exit()

def trim():
    # Remove surrounding double quotes and strip whitespace and line breaks
    sleep(0.1)
    prev_content = clipboard.paste()
    if str == type(prev_content):
        print("typed")
        trimmed = prev_content.strip(' "\r\n;')
        trimmed = trimmed.replace('`"`"', '`"')
        trimmed = trimmed.replace('; \r', ' \r')
        trimmed = trimmed.replace(';)', ')')
        trimmed = trimmed.replace('; )', ')')
        clipboard.copy(trimmed)
    print('<ctrl>+c is pressed')

def window_name():
    fw = pyautogui.getActiveWindow()
    print(fw.title)

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_h,
        '<esc>': on_activate_i,
        '<ctrl>+<alt>+w' : window_name,
        '<ctrl>+c': trim
            }) as h:
    h.join()