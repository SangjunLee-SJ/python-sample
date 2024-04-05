import cv2
from pyzbar import pyzbar

def read_qr_code(file_path):
    # Read the image
    image = cv2.imread(file_path)

    # Decode the QR code
    decoded_objects = pyzbar.decode(image)

    for obj in decoded_objects:
        # Print the type and data of the QR code
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))

if __name__ == "__main__":
    # Path to the QR code image
    image_path = "C:/Users/user/Downloads/QR_code.jpg"
    
    # Read and interpret the QR code
    read_qr_code(image_path)
