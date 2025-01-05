# coding: utf-8

import pyperclip
import pyautogui
import argparse
import time


def get_unicode_special() -> tuple[str, dict]:
    s = """
↑: up (U+2191)
↓: down (U+2193)
←: left (U+2190)
→: right (U+2192)
↵: enter (U+21B5)
⇧: shift (U+21E7)
⎈: ctrl (U+2388)
⎇: alt (U+2387)
⌫: backspace (U+232B)
⎋: esc (U+238B)
⬅: lmb=left-mouse-button (U+2B05)
➡: rmb=right-mouse-button (U+27A1)
❖: win (U+2756)
"""  # 🔃: mouse wheel (U+1F503)
    """
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
    """
    d = {
        "↑": "up",
        "↓": "down",
        "←": "left",
        "→": "right",
        "↵": "enter",
        "⇧": "shift",
        "⎈": "ctrl",
        "⎇": "alt",
        "⌫": "backspace",
        "⎋": "esc",
        "⬅": "lmb",
        "➡": "rmb",
        "❖": "win",
    }
    return s, d


def press_key(key: str, delay_between: int, delay_between_up_down: int):
    if key in {"lmb", "rmb"}:
        button_text = "left" if key == "lmb" else "right"
        pyautogui.mouseDown(button=button_text)
        time.sleep(delay_between_up_down / 1000)
        pyautogui.mouseUp(button=button_text)
        time.sleep(delay_between / 1000)
    else:
        pyautogui.keyDown(key)
        time.sleep(delay_between_up_down/1000)
        # pyautogui.press(key)
        pyautogui.keyUp(key)
        time.sleep(delay_between/1000)


def process(args: argparse.Namespace):
    if args.print_unicode_special:
        print(get_unicode_special()[0])
        exit()

    if args.ignore_unicode_special:
        unicode_special = {}
    else:
        unicode_special = get_unicode_special()[1]

    if args.clip_text is None:
        clipboard_text = pyperclip.paste()
    else:
        clipboard_text = args.clip_text
    if clipboard_text == "":
        print("Clipboard text in empty. ")
        exit()

    time.sleep(args.delay_before/1000)

    if args.terminal_duplicate:
        print("Typing: ", end="")

    for sym_i in clipboard_text:
        if sym_i in unicode_special:
            sym_i_to_type = unicode_special[sym_i]
        else:
            sym_i_to_type = sym_i

        press_key(sym_i_to_type, args.delay_between, args.delay_between_up_down)

        if args.terminal_duplicate:
            print(sym_i, end="")

    if args.terminal_duplicate:
        print()