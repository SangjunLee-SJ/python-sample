import tkinter as tk
from tkinter import filedialog, messagebox
import os
import chardet

class FolderMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Maker")
        
        # Create and place the button for making folders
        self.make_folders_button = tk.Button(root, text="Make Folders", command=self.make_folders)
        self.make_folders_button.pack(pady=20)
        
        # Create and place the label for displaying messages
        self.status_label = tk.Label(root, text="Prepare a text file with title text.")
        self.status_label.pack(pady=20)

    def get_unique_folder_name(self, base_path, base_name):
        counter = 1
        new_name = base_name
        while os.path.exists(os.path.join(base_path, new_name)):
            new_name = f"{base_name} ({counter})"
            counter += 1
        return new_name

    def detect_encoding(self, file_path):
        with open(file_path, 'rb') as f:
            raw_data = f.read(10000)  # Read first 10KB for detection
        result = chardet.detect(raw_data)
        return result['encoding']

    def make_folders(self):
        filepath = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])
        if not filepath:
            return
        
        try:
            encoding = self.detect_encoding(filepath)
            with open(filepath, "r", encoding=encoding) as f:
                titles = f.readlines()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read the file: {e}")
            return
        
        # Creating the main folder named after the text file
        base_folder_name = os.path.splitext(os.path.basename(filepath))[0]  # Extracting filename without extension
        main_folder_name = self.get_unique_folder_name(os.path.dirname(filepath), base_folder_name)
        main_folder_path = os.path.join(os.path.dirname(filepath), main_folder_name)
        os.makedirs(main_folder_path, exist_ok=True)
        
        for title in titles:
            title = title.strip()  # Remove any leading/trailing whitespaces
            if title:  # Ensure the title is not empty
                subfolder_name = self.get_unique_folder_name(main_folder_path, title)
                os.makedirs(os.path.join(main_folder_path, subfolder_name), exist_ok=True)

        self.status_label.config(text="Done.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderMakerApp(root)
    root.mainloop()
