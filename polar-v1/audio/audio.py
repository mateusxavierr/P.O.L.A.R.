import sounddevice
import soundfile
import uuid
import subprocess
import threading
from faster_whisper import WhisperModel
import ui.textbank as textbank

AUDIO_TIME = 5
AUDIO_FORMAT = 'WAV'
WHISPER_MODEL_SIZE = 'small'
BEAM_SIZE = 5


class Recorder:
    def record(
            self,
            audio_time: int=AUDIO_TIME,
            dtype: str='int16'
            ) -> None: 
        self.audio_data = sounddevice.rec(
            int(audio_time * 16000),
            samplerate=16000,
            dtype=dtype,
            channels=1
            )
        sounddevice.wait()

    def create_file(
            self,
            audio_path: str=None,
            audio_format: str=AUDIO_FORMAT
            ) -> None:
        if audio_path == None:
            audio_path = f'/tmp/{uuid.uuid4()}.wav'
        self.audio_path = audio_path
        
        try:
            soundfile.write(
                audio_path,
                self.audio_data,
                samplerate=16000,
                format=audio_format,
                subtype='PCM_16'
                )
        except Exception as e:
            print(textbank.MESSAGES[textbank.LANG]['audio_write_error'].format(error=e))


class Transcriber:
    def __init__(
            self,
            whisper_model: str=WHISPER_MODEL_SIZE,
            device: str='cpu'
            ) -> None: 
        self.engine = WhisperModel(
            whisper_model,
            device=device,
            compute_type='int8'
            )

    def transcribe(
            self,
            audio_path: str,
            beam_size: int=BEAM_SIZE,
            vad_filter: bool=True,
            condition_on_previous_text: bool=True
            ) -> None:
        
        try:
            self.segments, self.info = self.engine.transcribe(
                audio_path,
                beam_size=beam_size,
                vad_filter=vad_filter,
                condition_on_previous_text=condition_on_previous_text
                )
            self.language = getattr(self.info, 'language', 'en')
            if self.language in ['pt', 'pt-BR']:
                textbank.LANG = 'pt'
            else:
                textbank.LANG = 'en'
            
            self.transcription = ''
            
        except Exception as e:
            print(textbank.MESSAGES[textbank.LANG]['transcription_error'].format(error=e))
            self.segments = []
            self.info = None

    def text(self) -> str:
        for segment in self.segments:
            if segment.text.strip():
                self.transcription += segment.text

        return self.transcription
    
    def infos(self) -> str:
        prob = getattr(self.info, 'language_probability', 0.0) * 100

        if not self.info:
            return textbank.MESSAGES[textbank.LANG]['unknown_language']

        return textbank.MESSAGES[textbank.LANG]['language_detected'].format(lang=self.language, prob=prob)  


class Speaker:
    @staticmethod
    def speak(text: str, language: str) -> None:
        def _speak() -> None:
            voice = 'Felipe (Enhanced)' if language == 'pt' else 'Alex'

            try:
                subprocess.run(['say', '-v', voice, text], check=True)

            except Exception as e:
                print(textbank.MESSAGES[textbank.LANG]['voice_command_error'].format(error=e))

        threading.Thread(target=_speak).start()