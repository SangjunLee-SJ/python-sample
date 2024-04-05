import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk

def on_input(*args):
    value = text_var.get()
    if len(value) > 100:  # Limit input to 100 characters
        text_var.set(value[:100])

def generate_qr():
    # Get text from the input field
    text_content = text_var.get()
    if text_content:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text_content)
        qr.make(fit=True)
        global img  # Declare img as a global variable to use in the save_qr function
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Display QR code on the Tkinter GUI
        show_qr_code(img)

def show_qr_code(img):
    # Convert PIL image to a Tkinter compatible image
    tk_image = ImageTk.PhotoImage(img)
    qr_label.config(image=tk_image)
    qr_label.image = tk_image  # Keep a reference

def save_qr():
    # Save the image
    if 'img' in globals():
        img.save("qr_code.png")
        messagebox.showinfo("Save Successful", "The QR code has been saved as qr_code.png.")
    else:
        messagebox.showwarning("Save Failed", "Please generate a QR code first.")

# Setup Tkinter GUI
root = tk.Tk()
root.title("Convert Text to QR Code")

text_var = tk.StringVar()
text_var.trace("w", on_input)  # Trace changes to the string variable

# Text input field using Entry instead of Text for single line input
text_entry = ttk.Entry(root, textvariable=text_var, width=50)
text_entry.pack()

# 'Generate' button
generate_button = ttk.Button(root, text="Generate", command=generate_qr)
generate_button.pack()

# 'Save' button
save_button = ttk.Button(root, text="Save", command=save_qr)
save_button.pack()

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack()

root.mainloop()
