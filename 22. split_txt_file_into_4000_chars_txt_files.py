import chardet

def split_text_file(input_file, output_file_prefix, max_chars=4000):
    # Detect the file encoding
    with open(input_file, 'rb') as file:
        raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)['encoding']
    
    # Open the original file for reading with the detected encoding
    with open(input_file, 'r', encoding=detected_encoding) as file:
        text = file.read()
    
    # Calculate the number of parts needed
    num_parts = len(text) // max_chars + (1 if len(text) % max_chars != 0 else 0)
    
    # Split and write to new files
    for i in range(num_parts):
        start = i * max_chars
        end = start + max_chars
        part_text = text[start:end]
        
        # Write the chunk to a new file
        output_file = f"{output_file_prefix}_part_{i + 1}.txt"
        with open(output_file, 'w', encoding='utf-8') as part_file:
            part_file.write(part_text)
        
        print(f"Created: {output_file}")

# Example usage:
input_file = r'txt file path/.txt'  # Replace with your input file path
output_file_prefix = 'output'  # Prefix for output files
split_text_file(input_file, output_file_prefix)
