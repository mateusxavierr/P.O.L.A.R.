import requests
import ui.textbank as textbank

ROUTE = 'http://localhost:11434/api/generate'
MODEL = 'openhermes'
SYSTEM_MESSAGE = 'Você é o Polar, um assistente virtual. Seja sempre estratégico, conciso, minimalista.'
STREAM = False


class AI:
    def __init__(
            self,
            route: str=ROUTE,
            model: str=MODEL,
            system_message: str=SYSTEM_MESSAGE,
            stream: bool=STREAM
            ) -> None:
        self.route = route
        self.model = model
        self.system_message = system_message
        self.stream = stream
        self.response = None
        self.status_code = None

    def ask(self, prompt: str) -> None:
        self.prompt = prompt

        try:
            response = requests.post(self.route, json={
                'model': self.model,
                'system': self.system_message,
                'prompt': self.prompt,
                'stream': self.stream
                })
            
            self.status_code = response.status_code

            if self.status_code == 200:
                self.response = response.json()['response'].strip()
            
            else:
                self.response = textbank.MESSAGES[textbank.LANG]['no_response']

        except Exception as e:
            print(textbank.MESSAGES[textbank.LANG]['request_error'].format(error=e))
            self.response = None
            self.status_code = 500

    def answer(self) -> str: 
        if self.response:
            return self.response
        
        if self.status_code is not None:
            return textbank.MESSAGES[textbank.LANG]['generic_error']