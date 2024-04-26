import os
from PIL import Image
from fpdf import FPDF

def convert_images_to_pdf(image_folder, pdf_path):
    # Get all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    # Sort images alphabetically
    image_files.sort()

    # Create a PDF object
    pdf = FPDF()

    # Iterate through each image
    for image_file in image_files:
        # Open the image using PIL
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        # Convert image to grayscale (optional)
        image = image.convert('RGB')
        # Add a page to the PDF
        pdf.add_page()
        # Get image dimensions
        width, height = image.size
        # Add the image to the PDF
        pdf.image(image_path, 0, 0, width, height)

    # Save the PDF to the specified path
    pdf.output(pdf_path, "F")

if __name__ == "__main__":
    # Prompt user for input folder and output PDF path
    input_folder = input("Enter the path to the folder containing images (png files): ")
    output_pdf = input("Enter the path to save the PDF file: ")

    # Check if the output path is a directory
    if os.path.isdir(output_pdf):
        # If the output path is a directory, prompt for a filename within that directory
        filename = input("Enter the filename for the PDF (without extension): ")
        output_pdf = os.path.join(output_pdf, f"{filename}.pdf")

    # Convert images to PDF
    convert_images_to_pdf(input_folder, output_pdf)
