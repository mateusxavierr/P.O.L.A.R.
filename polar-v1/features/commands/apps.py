import platform
import subprocess
from typing import Optional

def open_app(app_name: str) -> str:
    if platform.system() == 'Darwin':
        try:
            subprocess.run(['open', '-a', app_name])
            return f'{app_name} opened.'

        except Exception as e:
            return f'Failed to open {app_name}: {e}'

    else:
        return 'Opening apps is only supported on macOS.'


def open_from_command(command: str) -> Optional[str]:
    command = command.lower()

    APP_ALIASES = {
        'calendar': 'Calendar',
        'calendário': 'Calendar',
        'vs code': 'Visual Studio Code',
        'vscode': 'Visual Studio Code',
        'spotify': 'Spotify',
        'notas': 'Notes',
        'notes': 'Notes',
        'safari': 'Safari'
    }

    for alias, app in APP_ALIASES.items():
        if alias in command:
            open_app(app)
            return app

    return None
