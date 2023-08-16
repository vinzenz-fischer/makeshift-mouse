from pynput.keyboard import Key, Listener
from pynput.keyboard._win32 import KeyCode
import pyautogui as pag
pag.PAUSE = 0.01
active = False
speed = 20
listener: Listener

def keycode(char: str):
    return [KeyCode.from_char(char.lower()), KeyCode.from_char(char.upper())]

keybinds: dict[str, Key] = {
    "toggle active":Key.caps_lock,
    "move up":      keycode("w"),
    "move left":    keycode("a"),
    "move down":    keycode("s"),
    "move right":   keycode("d"),
    "click left":   keycode("w"),
    "click left":   keycode("q"),
    "click right":  keycode("e"),
    "click middle": keycode("r"),
    "scroll up":    keycode("f"),
    "scroll down":  keycode("c")
}

def on_press(key):
    global active, listener
    
    if key in keybinds["toggle active"]:
        active = not active
        listener._suppress = active
        print(f"{active=}")
    
    if not active: return
    
    if   key in keybinds["move up"]:      pag.move(0, -speed)
    elif key in keybinds["move left"]:    pag.move(-speed, 0)
    elif key in keybinds["move down"]:    pag.move(0,  speed)
    elif key in keybinds["move right"]:   pag.move( speed, 0)
    elif key in keybinds["click left"]:   pag.click(button=pag.LEFT)
    elif key in keybinds["click right"]:  pag.click(button=pag.RIGHT)
    elif key in keybinds["click middle"]: pag.click(button=pag.MIDDLE)
    elif key in keybinds["scroll up"]:    pag.scroll(10)
    elif key in keybinds["scroll down"]:  pag.scroll(-10)

def main():
    global listener
    listener = Listener(on_press=on_press)
    with listener:
        listener.join()

if __name__ == "__main__":
    main()