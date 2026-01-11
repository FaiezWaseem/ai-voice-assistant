# AI Voice Assistant

A Python-based voice assistant that facilitates voice-to-voice interaction. It records your speech, transcribes it using ElevenLabs, generates an intelligent audio response using Pollinations AI, and plays it back to you.

## Features

- **Smart Recording**: Automatically detects when you start and stop speaking using silence detection.
- **High-Quality Transcription**: Uses **ElevenLabs Scribe v2** for accurate Speech-to-Text (STT) conversion.
- **AI Response & Synthesis**: leverages **Pollinations AI** (using the `openai-audio` model) to generate both a text response and natural-sounding speech in one step.
- **Audio Playback**: Automatically plays back the generated response.

## Prerequisites

- Python 3.8 or higher
- [FFmpeg](https://ffmpeg.org/download.html) (Required for audio playback functionalities)

## Installation

1. **Clone the repository** (or download the files).

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory.
2. Add your API keys:

   ```env
   ELEVEN_API_KEY=your_elevenlabs_api_key
   OPENAI_API_KEY=your_openai_api_key  # Optional for Pollinations, but recommended
   ```

   > **Note**: This project uses [Pollinations.ai](https://pollinations.ai) which provides free access to OpenAI-compatible models, but you may need an API key for higher limits or stability.

## Usage

Run the main script to start the assistant:

```bash
python main.py
```

1. The script will calibrate background noise (stay silent for 1 second).
2. Speak into your microphone.
3. The assistant will transcribe your speech and reply with audio.

## File Structure

- `main.py`: Entry point of the application. Orchestrates recording, transcription, and response.
- `record_audio.py`: Handles audio recording with silence detection.
- `eleven_lab.py`: Handles Speech-to-Text using ElevenLabs API.
- `tts.py`: Handles Text-to-Audio/Response generation using Pollinations AI.
- `play.py`: Handles audio playback.
- `audio/`: Directory where temporary audio files (`input.wav`, `output.wav`) are stored.
