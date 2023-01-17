# Extract filenames(Python)
# THIS CODE IS SUPPORTED BY ChatGPT and Copliot

import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(title = "Select Folder to Extract file names(txt will be saved in the same folder)")

# get a list of all the files in the folder
files = os.listdir(folder_path)

# extract the filenames of the files
filenames = [file for file in files]

# specify the location to save the extracted filenames
file_path = os.path.join(folder_path, "filenames_extracted.txt")

# save the filenames in a txt file
with open(file_path, "w") as f:
    for filename in filenames:
        f.write(filename + "\n")