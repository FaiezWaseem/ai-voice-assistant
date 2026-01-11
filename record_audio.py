import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def record_audio(duration=5, fs=44100, filename='audio/input.wav'):
    print(f"Recording for {duration} seconds...")
    
    # Ensure audio directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Record audio
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    
    print("Recording finished. Saving to file...")
    
    # Converting to 16-bit PCM for better compatibility
    data_int16 = (myrecording * 32767).astype(np.int16)
    
    write(filename, fs, data_int16)
    print(f"Saved to {filename}")
    return filename
