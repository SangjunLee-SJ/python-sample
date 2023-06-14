import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from datetime import timedelta

class AudioEditor:
    def __init__(self, root):
        self.root = root
        self.file_path = None
        self.audio = None
        self.timestamp = 0

        self.create_widgets()

    def create_widgets(self):
        self.open_button = tk.Button(self.root, text="Open File", command=self.open_file_dialog)
        self.open_button.pack()

        self.timestamp_entry = tk.Entry(self.root)
        self.timestamp_entry.pack()

        self.timestamp_bar = tk.Scale(self.root, orient="horizontal", command=self.update_timestamp)
        self.timestamp_bar.pack()

        self.divide_button = tk.Button(self.root, text="Divide", command=self.divide_audio)
        self.divide_button.pack()

    def open_file_dialog(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.m4a")])
        if self.file_path:
            self.audio = AudioSegment.from_file(self.file_path, format="m4a")
            self.timestamp_bar.config(to=len(self.audio) - 1, resolution=1)  # Set timestamp bar range

    def update_timestamp(self, value):
        self.timestamp = int(value)
        self.timestamp_entry.delete(0, tk.END)  # Clear the entry field
        timestamp_str = str(timedelta(milliseconds=self.timestamp))  # Convert timestamp to hh:mm:ss
        timestamp_str = timestamp_str.split('.')[0]  # Remove the decimal part
        self.timestamp_entry.insert(0, timestamp_str)  # Insert the new timestamp

    def divide_audio(self):
        if self.audio:
            first_half = self.audio[:self.timestamp]
            second_half = self.audio[self.timestamp:]

            save_path1 = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
            if save_path1:
                first_half.export(save_path1, format="mp3")

            save_path2 = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
            if save_path2:
                second_half.export(save_path2, format="mp3")

# Create Tkinter window
root = tk.Tk()
root.title("Audio Editor")
app = AudioEditor(root)

# Start the Tkinter event loop
root.mainloop()
