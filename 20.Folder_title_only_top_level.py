# Folder name only, Top level only

import os

def save_top_level_folders(input_directory, output_directory):
    output_file_path = os.path.join(output_directory, 'folderlist.txt')
    with open(output_file_path, 'w') as file:
        for root, dirs, files in os.walk(input_directory):
            if root == input_directory:
                for dir_name in dirs:
                    file.write(dir_name + '\n')
            break

if __name__ == "__main__":
    print("Enter input directory:")
    input_directory = input()
    print("Enter save file path:")
    output_directory = input()

    if not os.path.exists(input_directory):
        print(f"The directory {input_directory} does not exist.")
    elif not os.path.exists(output_directory):
        print(f"The directory {output_directory} does not exist.")
    else:
        save_top_level_folders(input_directory, output_directory)
        print(f'Top-level folder names have been saved to {os.path.join(output_directory, "folderlist.txt")}')
