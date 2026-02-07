import pyttsx3

class VoiceEngine:
    def __init__(self, voice_id=None):
        # Initialize the TTS engine
        self.engine = pyttsx3.init()
        if voice_id:
            self.set_voice(voice_id)

    def set_voice(self, voice_id):
        """Set the voice for text-to-speech."""
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if voice.id == voice_id:
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text):
        """Convert text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

# Example usage
if __name__ == "__main__":
    voice_engine = VoiceEngine()  # You can pass a custom voice ID if needed
    voice_engine.speak("Hello, this is a custom voice speaking!")
