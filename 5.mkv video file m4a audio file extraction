import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def get_ffmpeg_progress(output):
    # Extract the progress information from ffmpeg's output
    for line in output.splitlines():
        if "time=" in line:
            # Extract the current time value
            time = line.split("time=")[-1].split(" ")[0]
            h, m, s = time.split(":")
            total_seconds = int(h) * 3600 + int(m) * 60 + float(s)
            return total_seconds
    return 0

def extract_audio_from_video(video_file, audio_file):
    command = [
        'ffmpeg', 
        '-i', video_file, 
        '-vn', 
        '-acodec', 'copy',
        '-y',  # Overwrite output file if it exists
        audio_file
    ]
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, bufsize=1)
    duration = None
    
    for line in iter(process.stdout.readline, ''):
        if "Duration:" in line:
            duration = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = duration.split(":")
            duration = int(h) * 3600 + int(m) * 60 + float(s)
        elif "time=" in line and duration:
            current_time = get_ffmpeg_progress(line)
            progress = (current_time / duration) * 100
            progress_var.set(progress)
            root.update()

def on_browse():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mkv;*.mp4;*.avi;*.flv")])
    
    if not file_path:
        return

    output_file_path = file_path.rsplit(".", 1)[0] + ".m4a"
    extract_audio_from_video(file_path, output_file_path)

root = tk.Tk()
root.title("Audio Extractor")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

browse_button = ttk.Button(frame, text="Browse Video File", command=on_browse)
browse_button.grid(row=0, column=0, pady=10, sticky=tk.W)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate", variable=progress_var)
progress_bar.grid(row=1, column=0, pady=10)

root.mainloop()
