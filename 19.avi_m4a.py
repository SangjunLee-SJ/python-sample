# python avi_m4a.py "C:\path\to\your\input_video.avi"
import subprocess
import os
import sys

def extract_audio(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return False

    command = [
        'ffmpeg',
        '-i', input_file,
        '-vn',  # Disable video
        '-acodec', 'aac',  # Use AAC codec for audio
        '-b:a', '192k',  # Set audio bitrate
        '-y',  # Overwrite output file if it exists
        output_file
    ]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Print ffmpeg output in real-time
        for line in process.stdout:
            print(line, end='')

        process.wait()

        if process.returncode == 0:
            print(f"\nSuccessfully extracted audio to {output_file}")
            return True
        else:
            print(f"\nError: ffmpeg process returned non-zero exit status {process.returncode}")
            return False

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_avi_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + ".m4a"

    success = extract_audio(input_file, output_file)
    sys.exit(0 if success else 1)
