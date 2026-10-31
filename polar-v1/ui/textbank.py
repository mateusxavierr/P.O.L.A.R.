LANG = 'en'
ACTION_WORDS = {
    'pt': [
        'abrir', 'abre', 'inicia', 'iniciar', 'começar', 'executar', 'rodar',
        'liga', 'lança', 'chama', 'acessa', 'carrega', 'entrar no', 'abre aí',
        'vai para', 'ativa', 'ativar', 'ative'
    ],
    'en': [
        'open', 'start', 'launch', 'run', 'begin', 'access', 'load',
        'execute', 'go to', 'fire up', 'bring up', 'turn on', 'call',
        'activate', 'pull up'
    ]
}

CLOSE_WORDS = {
    'pt': [
        'fechar', 'parar', 'encerra', 'encerrar', 'desliga', 'desligar',
        'termina', 'terminar', 'desativa', 'desativar', 'sair do', 'sair',
        'finaliza', 'finalizar'
    ],
    'en': [
        'close', 'stop', 'exit', 'quit', 'shutdown', 'end', 'terminate',
        'deactivate', 'leave', 'turn off'
    ]
}

MESSAGES = {
    'pt': {
        'unknown_language': 'Idioma: desconhecido (0.00%)',
        'language_detected': 'Idioma detectado: {lang} ({prob:.2f}%)',
        'transcription_error': 'Erro na transcrição: {error}',
        'audio_write_error': 'Erro ao criar arquivo de áudio: {error}',
        'voice_command_error': 'Erro ao executar comando de voz: {error}',
        'request_error': 'Erro na requisição: {error}',
        'no_response': 'Sem resposta.',
        'generic_error': 'Erro. Tente novamente.',
        'double_option_detected': 'Duplo toque no Option detectado.',
        'recording': 'Gravando...',
        'recording_done': 'Gravação finalizada.',
        'transcription': 'Transcrição:',
        'ai_response': 'Resposta da IA:',
        'app_opened': ' foi aberto.',
        'command_not_found': 'Aplicativo ou modo não encontrado.',
        'mode_started': 'foi iniciado.',
        'close_mode_error': 'Erro ao tentar fechar o modo.',
        'mode_closed': 'foi encerrado.',
        'duration': 'Duração:',
        'minutes': 'minutos.',
        'chronometer_running': 'Cronômetro já iniciado.',
    },
    'en': {
        'unknown_language': 'Language: unknown (0.00%)',
        'language_detected': 'Detected language: {lang} ({prob:.2f}%)',
        'transcription_error': 'Transcription error: {error}',
        'audio_write_error': 'Error writing audio file: {error}',
        'voice_command_error': 'Error running voice command: {error}',
        'request_error': 'Request error: {error}',
        'no_response': 'No response.',
        'generic_error': 'Error. Please try again.',
        'double_option_detected': 'Double Option key press detected.',
        'recording': 'Recording...',
        'recording_done': 'Recording finished.',
        'transcription': 'Transcription:',
        'ai_response': 'AI response:',
        'app_opened': 'launched.',
        'command_not_found': 'App or mode not found.',
        'mode_started': 'mode was activated.',
        'close_mode_error': 'Error trying close the mode.',
        'mode_closed': 'mode was deactivated.',
        'duration': 'Duration:',
        'minutes': 'minutes.',
        'chronometer_running': 'Chronometer already running.',
    }
}