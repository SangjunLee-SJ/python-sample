# Change filenames using xlsx(Python)
# ThIS CODE IS SUPPORTED BY ChatGPT and Copliot
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(title = "Select Folder to change file names")
excel_file = filedialog.askopenfilename(title = "Select Excel File that contains the original and new file names")

# read the excel file
df = pd.read_excel(excel_file)

# iterate through the dataframe and rename the files
for i, row in df.iterrows():
    original_filename = row['original_filename']
    new_filename = row['new_filename']
    new_filename = new_filename.replace("/", "-")
    old_path = os.path.join(folder_path, original_filename)
    
    # replace characters cannot used in os path
    if os.path.isfile(old_path):    
        new_path = os.rename(old_path, os.path.join(folder_path, new_filename))
    else:
        print(f"{original_filename} not found in {folder_path}")
        print(f"{new_filename} contains invalid characters")