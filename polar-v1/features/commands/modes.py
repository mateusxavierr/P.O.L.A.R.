import subprocess
from pathlib import Path
from .time import TimeManager
from typing import Optional

time = TimeManager()

MODES_ALIASES = {
        'focus': 'focus',
        'foco': 'focus'
    }

def activate(mode: str) -> None:
    focus_script = Path(__file__).parent.parent / 'modes-scripts' / f'{mode}.scpt'
    try:
        subprocess.run(['osascript', str(focus_script)])
        time.start_chronometer()
    except Exception as e:
        print(f'Failed to activate {mode} mode: {e}')##############

def deactivate(mode: str) -> None:
    try:
        duration = time.stop_chronometer()
        return duration
    except Exception as e:
        print(f'Failed to deactivate mode: {e}')

def open_from_command(command: str) -> Optional[tuple]:
    command = command.lower()

    for alias, mode in MODES_ALIASES.items():
        if alias in command:
            activate(mode)
            return mode, alias
    return None

def close_from_command(command: str) -> Optional[tuple]:
    command = command.lower()

    for alias, mode in MODES_ALIASES.items():
        if alias in command:
            duration = deactivate(mode)
            return mode, alias, duration
    return None