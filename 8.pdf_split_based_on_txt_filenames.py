import PyPDF2

def get_input_path(prompt_text):
    """
    Get file path input from the user.
    """
    return input(prompt_text)

def read_txt_file(txt_path):
    """
    Read the txt file and return list of lines.
    Try multiple encodings in case of Unicode errors.
    """
    encodings = ['utf-8', 'cp949', 'euc-kr', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            with open(txt_path, 'r', encoding=encoding) as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except UnicodeDecodeError:
            pass
    raise Exception("Failed to decode the file with provided encodings.")

def split_pdf(pdf_path, txt_path, output_folder):
    """
    Split the PDF into multiple files based on names.
    """
    # Read the txt file for names
    names = read_txt_file(txt_path)
    
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            output_filename = names[page_num] if page_num < len(names) else f"page_{page_num + 1}"
            # Ensure the filename ends with .pdf
            if not output_filename.endswith('.pdf'):
                output_filename += '.pdf'
            output_path = f"{output_folder}/{output_filename}"
            with open(output_path, 'wb') as output:
                writer = PyPDF2.PdfWriter()
                writer.add_page(page)
                writer.write(output)

def main_terminal():
    # Get paths from user input
    pdf_path = get_input_path("Enter the path of the PDF file: ")
    txt_path = get_input_path("Enter the path of the TXT file: ")
    output_folder = get_input_path("Enter the path of the folder to save split PDFs: ")
    
    # Split the PDF
    split_pdf(pdf_path, txt_path, output_folder)

# Run the main function
if __name__ == "__main__":
    main_terminal()
