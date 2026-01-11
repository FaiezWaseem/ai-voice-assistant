from elevenlabs import ElevenLabs
from elevenlabs.play import play

def play_audio(file_path):
    with open(file_path, 'rb') as f:
        audio_data = f.read()
        play(audio_data)


