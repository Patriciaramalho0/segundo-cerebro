import speech_recognition as sr
import pyttsx3
import os

class VoiceEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        # Configuração básica do TTS
        self.tts_engine.setProperty('rate', 180)
        voices = self.tts_engine.getProperty('voices')
        # Tenta selecionar uma voz masculina padrão (Daniel) se disponível
        for voice in voices:
            if 'Daniel' in voice.name or 'Male' in voice.name:
                self.tts_engine.setProperty('voice', voice.id)
                break

    def listen(self, timeout=5, phrase_time_limit=15):
        """Captura áudio do microfone e converte em texto."""
        try:
            with sr.Microphone() as source:
                # Ajusta para o ruído ambiente
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Ouvindo...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                
                print("Processando...")
                text = self.recognizer.recognize_google(audio, language="pt-BR")
                return text
        except sr.WaitTimeoutError:
            return "[Tempo esgotado]"
        except sr.UnknownValueError:
            return "[Não entendi a fala]"
        except Exception as e:
            return f"[Erro no microfone: {str(e)}]"

    def speak(self, text):
        """Converte texto em fala."""
        # Limpeza básica para evitar erros no TTS
        clean_text = text.replace('*', '').replace('#', '').replace('`', '')
        self.tts_engine.say(clean_text)
        self.tts_engine.runAndWait()