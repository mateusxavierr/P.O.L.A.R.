from audio.audio import Recorder, Transcriber, Speaker
from ui.hotkey import Hotkey
from core.ai import AI
import warnings
import numpy
import ui.textbank as textbank

warnings.filterwarnings('ignore', category=RuntimeWarning)
numpy.seterr(all='ignore')

recorder = Recorder()
transcriber = Transcriber()
speaker = Speaker()
ai = AI()


def execute() -> None:
    print(textbank.MESSAGES[textbank.LANG]['recording'])
    recorder.record()
    recorder.create_file()
    print(textbank.MESSAGES[textbank.LANG]['recording_done'])

    transcriber.transcribe(recorder.audio_path)
    print(transcriber.infos())
    print('\n' + textbank.MESSAGES[textbank.LANG]['transcription'])
    print(transcriber.text())

    ai.ask(transcriber.transcription)
    print('\n' + textbank.MESSAGES[textbank.LANG]['ai_response'])
    print(ai.response)
    
    speaker.speak(ai.response, transcriber.language)
        
hotkey = Hotkey(execute)

def run():
    hotkey.listener()