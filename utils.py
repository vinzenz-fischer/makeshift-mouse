from pynput.keyboard import KeyCode, Key

class Keybind:
    def __init__(self, key: Key|str) -> None:
        self.key = set()
        
        if type(key) == Key:
            self.key.add(key)
        elif type(key) == str:
            self.key.add(KeyCode.from_char(key.lower()))
            self.key.add(KeyCode.from_char(key.upper()))
    
    def __eq__(self, __other: Key|KeyCode) -> bool:
        return __other in self.key