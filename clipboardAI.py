from pynput import keyboard
import win32api
import clipboard

def on_activate_h():
    win32api.WinExec("calc.exe")
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<esc>')
    exit()

def trim():
    # Remove surrounding double quotes and strip whitespace and line breaks
    prev_content = clipboard.paste()
    trimmed = prev_content.strip(' "\t\n\r')
    clipboard.copy(trimmed)
    print('<ctrl>+<alt>+s is pressed')

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_h,
        '<esc>': on_activate_i,
        '<ctrl>+<alt>+s': trim}) as h:
    h.join()