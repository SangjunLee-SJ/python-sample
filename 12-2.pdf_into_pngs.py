# pip install PyMuPDF
import fitz  # PyMuPDF
import os

def convert_pdf_folder_to_images(source_folder, target_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith(".pdf"):
            source_path = os.path.join(source_folder, filename)
            document = fitz.open(source_path)
            
            for page_number in range(len(document)):
                page = document.load_page(page_number)
                image = page.get_pixmap()
                image_path = os.path.join(target_folder, f"{os.path.splitext(filename)[0]}_page_{page_number + 1}.png")
                image.save(image_path)
            document.close()

# 사용 예:
source_folder = 'C:/Users/user/Downloads/a'
target_folder = 'C:/Users/user/Downloads/b'
convert_pdf_folder_to_images(source_folder, target_folder)
