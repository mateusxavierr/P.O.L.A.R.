import threading
import time
import os
from typing import Callable
import ui.textbank as textbank


# TimeManager utility for timers, chronometer, and pomodoro
class TimeManager:
    def __init__(self) -> None:
        self._chronometer_running = False
        self._pomodoro_running = False
        self._start_time = None

    def _say(self, message: str) -> None:
        os.system(f'say "{message}"')

    def start_chronometer(self) -> None:
        if self._chronometer_running:
            print(textbank.MESSAGES[textbank.LANG]["chronometer_running"])
            return
        
        else:
            self.clock = '00:00'

            def run():
                s = 0

                while self._chronometer_running:
                    min, sec = divmod(s, 60)
                    self.clock = f'{min:02d}:{sec:02d}'
                    # print(self.clock, end='\r')
                    s += 1
                    time.sleep(1)

            self._start_thread(run, mode='chronometer')

    def stop_chronometer(self) -> str:
        self._chronometer_running = False

        if self._thread_chronometer and self._thread_chronometer.is_alive():
            self._thread_chronometer.join()
            return self.clock
        
    def _start_thread(self, target_func:Callable, mode:str) -> None:
        if mode == 'chronometer':
            if self._chronometer_running:
                print(textbank.MESSAGES[textbank.LANG]["chronometer_running"])
                return
            else:
                self._chronometer_running = True
                self._thread_chronometer = threading.Thread(target=target_func, daemon=True)
                self._thread_chronometer.start()