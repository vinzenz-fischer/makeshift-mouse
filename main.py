from pynput.keyboard import Listener, KeyCode
import pyautogui as pag
from settings import *

pag.PAUSE = 0.01
active = False
speed = 20
listener: Listener

def on_press(key: KeyCode|Key):
    global active, listener

    if Keybinds.TOGGLE_ACTIVE == key:
        active = not active
        listener._suppress = active
        print(f"{active=}")
    
    if not active: return
    
    if Keybinds.MOVE_UP      == key: pag.move(0, -speed)
    if Keybinds.MOVE_LEFT    == key: pag.move(-speed, 0)
    if Keybinds.MOVE_DOWN    == key: pag.move(0,  speed)
    if Keybinds.MOVE_RIGHT   == key: pag.move( speed, 0)
    if Keybinds.CLICK_LEFT   == key: pag.mouseDown(button=pag.LEFT)
    if Keybinds.CLICK_RIGHT  == key: pag.mouseDown(button=pag.RIGHT)
    if Keybinds.CLICK_MIDDLE == key: pag.mouseDown(button=pag.MIDDLE)
    if Keybinds.SCROLL_UP    == key: pag.scroll(10)
    if Keybinds.SCROLL_DOWN  == key: pag.scroll(-10)

def on_release(key: KeyCode|Key):
    if Keybinds.CLICK_LEFT   == key: pag.mouseUp(button=pag.LEFT)
    if Keybinds.CLICK_RIGHT  == key: pag.mouseUp(button=pag.RIGHT)
    if Keybinds.CLICK_MIDDLE == key: pag.mouseUp(button=pag.MIDDLE)

def main():
    global listener
    listener = Listener(on_press=on_press, on_release=on_release)
    with listener:
        listener.join()

if __name__ == "__main__":
    main()
