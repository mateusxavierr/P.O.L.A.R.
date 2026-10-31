import features.commands.apps as apps
import features.commands.modes as modes
from audio.audio import Recorder, Transcriber, Speaker
from core.ai import AI
import core.memory as memory
import warnings
import ui.textbank as textbank
# from ui.hotkey import Hotkey

warnings.filterwarnings('ignore', category=RuntimeWarning)

recorder = Recorder()
transcriber = Transcriber()
speaker = Speaker()
ai = AI()


def execute() -> None:
    while True:
        text_input = input('\nP.O.L.A.R.: ')
        if text_input.strip():
            user_input = text_input.strip()
        else:
            print(textbank.MESSAGES[textbank.LANG]['recording'])
            recorder.record()
            recorder.create_file()
            print(textbank.MESSAGES[textbank.LANG]['recording_done'])

            transcriber.transcribe(recorder.audio_path)
            detected = getattr(transcriber, 'language', None)
            if detected == 'pt':
                textbank.LANG = 'pt'
            else:
                textbank.LANG = 'en'

            print(transcriber.infos())
            print('\n' + textbank.MESSAGES[textbank.LANG]['transcription'])
            print(transcriber.text())
            user_input = transcriber.transcription

        if 'speak_lang' not in locals():
            speak_lang = getattr(transcriber, 'language', None)
            if speak_lang not in ('pt', 'en'):
                speak_lang = 'pt' if textbank.LANG == 'pt' else 'en'

        matched_word = next(
            (word for word in textbank.ACTION_WORDS[textbank.LANG] if word.lower() in user_input.lower()),
            None
        )
        close_word = next(
            (word for word in textbank.CLOSE_WORDS[textbank.LANG] if word.lower() in user_input.lower()),
            None
        )

        if close_word:
            try:
                mode_result = modes.close_from_command(user_input)
                closed_mode, mode_lang, mode_duration = mode_result
            except Exception:
                command_executed = None
                ai.response = textbank.MESSAGES[textbank.LANG]['close_mode_error']
            else:
                command_executed = f'{closed_mode.capitalize()} mode deactivated. Duration: {mode_duration}'
                ai.response = f'{mode_lang} {textbank.MESSAGES[textbank.LANG]["mode_closed"]} {textbank.MESSAGES[textbank.LANG]["duration"]} {mode_duration} {textbank.MESSAGES[textbank.LANG]["minutes"]}'

            print('\n' + textbank.MESSAGES[textbank.LANG]['ai_response'])
            print(ai.response)
            speaker.speak(ai.response, speak_lang)

        elif matched_word:
            opened_app = apps.open_from_command(user_input)
            mode_result = modes.open_from_command(user_input)

            if opened_app:
                command_executed = f'{opened_app} was launched.'
                ai.response = f'{opened_app.capitalize()} {textbank.MESSAGES[textbank.LANG]["app_opened"]}'
            elif mode_result:
                started_mode, mode_lang = mode_result
                command_executed = f'{started_mode.capitalize()} mode activated.'
                ai.response = f'{mode_lang} {textbank.MESSAGES[textbank.LANG]["mode_started"]}'
            else:
                command_executed = None
                ai.response = textbank.MESSAGES[textbank.LANG]['command_not_found']

            print('\n' + textbank.MESSAGES[textbank.LANG]['ai_response'])
            print(ai.response)
            speaker.speak(ai.response, speak_lang)

        else:
            command_executed = None
            ai.ask(user_input)
            print('\n' + textbank.MESSAGES[textbank.LANG]['ai_response'])
            print(ai.response)
            speaker.speak(ai.response, speak_lang)

        memory.table()
        memory.insert_interaction(user_input, ai.response, command_executed)
        
# hotkey = Hotkey(execute)

# def run() -> None:
#     hotkey.listener()