import tkinter as tk
from tkinter import filedialog
import base64
from io import BytesIO
from PIL import Image, ImageTk, ImageFile

# Enable loading of truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

def base64_to_image(base64_string):
    decoded_image = base64.b64decode(base64_string)
    image = Image.open(BytesIO(decoded_image))
    return image

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            base64_encoded_image = file.read().replace("\n", "").replace(" ", "")
            try:
                decoded_image = base64_to_image(base64_encoded_image)
                show_image(decoded_image)
            except Exception as e:
                status_label.config(text=f"Error decoding image: {str(e)}")


def show_image(image):
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

# GUI 생성
root = tk.Tk()
root.title("Base64 Image Decoder")

# 파일 열기 버튼
open_button = tk.Button(root, text="Open Base64 txt File", command=open_file_dialog)
open_button.pack(pady=10)

# 이미지 표시 레이블
image_label = tk.Label(root)
image_label.pack()

# 상태 표시 레이블
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# GUI 실행
root.mainloop()
