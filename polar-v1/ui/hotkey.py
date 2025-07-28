from pynput import keyboard
import time
import ui.textbank as textbank

DOUBLE_PRESS_THRESHOLD = 0.4


class Hotkey:
    def __init__(
            self,
            func,
            key_1: keyboard.Key=keyboard.Key.alt_l,
            key_2: keyboard.Key=keyboard.Key.alt_r,
            double_press_threshold: float=DOUBLE_PRESS_THRESHOLD
            ) -> None:
        self.key_1 = key_1
        self.key_2 = key_2
        self.double_press_threshold = double_press_threshold
        self.last_opt_time = 0
        self.triggered = False
        self.func = func

    def on_press(self, key) -> bool:
        if key == self.key_1 or key == self.key_2:
            now = time.time()
            if now - self.last_opt_time <= self.double_press_threshold:
                print('\n' + textbank.MESSAGES[textbank.LANG]['double_option_detected'] + '\n')
                self.last_opt_time = 0
                self.triggered = True
                self.func()
                
            else:
                self.last_opt_time = now
                
        return True

    def listener(self) -> None:
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()