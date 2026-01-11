from dotenv import load_dotenv
from tts import text_to_audio
from play import play_audio
from record_audio import record_audio
from eleven_lab import transcribe_audio
# Load environment variables
load_dotenv()


if __name__ == "__main__":
    # You can change the duration here
    INPUT_FILENAME = "audio/input.wav"
    
    # 1. Record (Smart Silence Detection)
    recorded_file = record_audio(filename=INPUT_FILENAME)
    
    # 2. Transcribe
    transcript = transcribe_audio(recorded_file)
    print(transcript)
    output_file = 'audio/output.wav'
    
    if transcript:
        # 3. Think (Generate Answer)
        answer = text_to_audio(transcript, output_file)
        print(answer)
        
        if answer:
            play_audio(output_file)
