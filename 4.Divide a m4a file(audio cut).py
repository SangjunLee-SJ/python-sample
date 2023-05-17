import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

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

    def divide_audio(self):
        if self.audio:
            first_half = self.audio[:self.timestamp]
            second_half = self.audio[self.timestamp:]

            first_half.export("output1.wav", format="wav")
            second_half.export("output2.wav", format="wav")

            # Convert WAV files to M4A using pydub
            output1 = AudioSegment.from_file("output1.wav", format="wav")
            output1.export("output1.m4a", format="m4a")

            output2 = AudioSegment.from_file("output2.wav", format="wav")
            output2.export("output2.m4a", format="m4a")

            print("Audio divided at timestamp:", self.timestamp)

# Create Tkinter window
root = tk.Tk()
root.title("Audio Editor")
app = AudioEditor(root)

# Start the Tkinter event loop
root.mainloop()
