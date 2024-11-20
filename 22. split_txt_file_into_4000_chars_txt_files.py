def split_text_file(input_file, output_file_prefix, max_chars=4000):
    # Open the original file for reading
    with open(input_file, 'r', encoding='utf-8') as file:
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
input_file = 'txt file path'  # Replace with your input file path
output_file_prefix = 'output'  # Prefix for output files #Warning: the output txt files will be saved in the location path of the python script has run.
split_text_file(input_file, output_file_prefix)
