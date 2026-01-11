from dotenv import load_dotenv
import json
from nt import write
import requests
import base64
import os
# from play import play_audio
load_dotenv()


# Configuration
API_URL = "https://gen.pollinations.ai/v1/chat/completions"
# Replace with your secret key from enter.pollinations.ai if you have one
# Basic requests may work without a key but are subject to lower limits.
HEADERS = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}

def text_to_audio(text, file_path='audio/output.wav'):

    payload = {
        "model": "openai-audio",
        "modalities": ["text", "audio"],
        "audio": { "voice": "alloy", "format": "wav" },
        "messages": [
            {
                "role": "system",
                "content":  "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content":  text,
            }
        ]
    }

    response = requests.post(API_URL, json=payload, headers=HEADERS)
    # print(response.json())
    # with open("response.json", "w") as f:
    #     json.dump(response.json(), f, indent=2)

    if response.status_code == 200:
        audio_response = response.json()['choices'][0]['message']['audio']
        audio_base64 = audio_response['data']
        # Decode the base64 audio data
        audio_data = base64.b64decode(audio_base64)
        # Save the audio data to a file
        with open(file_path, "wb") as f:
            f.write(audio_data)
        # Print the transcript
        return audio_response['transcript']
    else:
        return f"Error {response.status_code}: {response.text}"

# Example usage
# audio_file = 'audio/output_P.wav'
# result = text_to_audio("Hello, how are you?" , audio_file)
# print(result)
# play_audio(audio_file)
