import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
from elevenlabs.play import play

# Load environment variables
load_dotenv()

def speak_text(text, output_file='audio/output.mp3'):
    """Convert text to speech using ElevenLabs"""
    if not text:
        return
        
    eleven_api_key = os.getenv("ELEVEN_API_KEY")
    if not eleven_api_key:
        print("Error: ELEVEN_API_KEY not found in .env file.")
        return

    print("\nGenerating speech with ElevenLabs...")
    
    try:
        client = ElevenLabs(
            api_key=eleven_api_key
        )
        
        audio = client.text_to_speech.convert(
            text=text,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        
        # Save audio to file
        # The generate method returns a generator or bytes depending on configuration
        # Assuming bytes or iterator of bytes
        
        with open(output_file, 'wb') as f:
            for chunk in audio:
                f.write(chunk)
                
        print(f"Audio saved to {output_file}")
        
        # Play the audio
        # We can use simple playback here if we had a player, 
        # or just let the user know it's saved.
        # But 'elevenlabs' has a play function.
        # play(audio) # This streams it. Since we consumed the generator to save, we can't play it again easily without re-generating or playing the file.
        
        print("Playing audio...")
        # To play the saved file, we might need an external tool or read it back.
        # But for simplicity in this environment, let's just say it's saved.
        # However, the user asked to "answer as audio output".
        # Let's try to play it if possible.
        
        try:
            # Using sounddevice to play the file requires decoding mp3 which scipy/numpy don't do natively easily without lib.
            # So we will skip playing for now unless we use 'playsound' or similar, 
            # OR we can try to use elevenlabs.play(audio) BEFORE saving, or just regenerate for play? No that's wasteful.
            # Actually, elevenlabs.play() takes bytes.
            
            # Let's read the bytes back
            with open(output_file, 'rb') as f:
                audio_data = f.read()
                play(audio_data)
                
        except Exception as play_error:
            print(f"Could not play audio directly (might need ffmpeg installed): {play_error}")
            print("Please open the file manually to listen.")

    except Exception as e:
        print(f"ElevenLabs TTS error: {e}")



def transcribe_audio(filename):
    api_key = os.getenv("ELEVEN_API_KEY")
    # Use dummy key if not set, as custom endpoint might not require it
    if not api_key or api_key == "your_openai_api_key_here":
        api_key = "dummy"
    
    client = ElevenLabs(api_key=api_key)

    print(f"\nTranscribing audio with ELEVEN LABS AI...")
    
    try:
        audio_file_path = filename

        with open(audio_file_path, "rb") as audio_file:
            transcription = client.speech_to_text.convert(
                file=audio_file,
                model_id="scribe_v2",        # The current state-of-the-art model
                language_code="eng",         # Optional: defaults to auto-detect
                tag_audio_events=True,       # Captures laughter, applause, etc.
                diarize=True                 # Identifies different speakers
            )

        return transcription.text
        
    except Exception as e:
        print(f"Transcription error: {e}")
        return None
