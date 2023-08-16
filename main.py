from pynput.keyboard import Key, Listener
from pynput.keyboard._win32 import KeyCode
import pyautogui as pag
pag.PAUSE = 0.01
speed = 20
active = False

def keycode(key, char: str):
    return key == KeyCode.from_char(char.lower()) or key == KeyCode.from_char(char.upper())

def on_press(key):
    global active
    
    if key == Key.caps_lock:
        active = not active
        print(f"{active=}")
    
    if not active: return
    
    if   keycode(key, "w"): pag.move(0, -speed)
    elif keycode(key, "a"): pag.move(-speed, 0)
    elif keycode(key, "s"): pag.move(0,  speed)
    elif keycode(key, "d"): pag.move( speed, 0)
    elif keycode(key, "q"): pag.click(button=pag.LEFT)
    elif keycode(key, "e"): pag.click(button=pag.RIGHT)
    elif keycode(key, "r"): pag.click(button=pag.MIDDLE)
    elif keycode(key, "f"): pag.scroll(10)
    elif keycode(key, "c"): pag.scroll(-10)

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()