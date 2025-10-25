import os
import whisper
from tqdm import tqdm
import numpy as np

# Load the Whisper model
model = whisper.load_model("base", device="cpu")

# Path to the folder containing MP3 files
audio_folder = "C:/a/video/input"  # 폴더 경로 수정
output_folder = "C:/a/video/output"  # 결과 저장 폴더 경로

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get a list of all MP3 files in the folder
audio_files = [f for f in os.listdir(audio_folder) if f.endswith(".mp3")]

# Process each MP3 file
for audio_file in tqdm(audio_files, desc="Processing files"):
    # Full path to the audio file
    audio_path = os.path.join(audio_folder, audio_file)
    
    # Transcribe the entire file
    #result = model.transcribe(audio_path, language='en', verbose=True, condition_on_previous_text=True)
    result = model.transcribe(audio_path, language='ko', verbose=True, condition_on_previous_text=True)
    # Output text file path based on audio file name
    output_file = os.path.join(output_folder, f"{os.path.splitext(audio_file)[0]}_transcription.txt")
    
    # Write the transcribed text to the text file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Transcription for {audio_file} saved to {output_file}")

print("All files processed successfully.")
