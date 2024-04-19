import os

def save_file_paths(input_directory, output_directory):
    output_file_path = os.path.join(output_directory, 'filelist.txt')
    with open(output_file_path, 'w') as file:
        for root, dirs, files in os.walk(input_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file.write(file_path + '\n')

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
        save_file_paths(input_directory, output_directory)
        print(f'File paths have been saved to {os.path.join(output_directory, "filelist.txt")}')



# or use the below python code to run like python script.py <input_directory> <output_directory>
# import os
# import sys

# def save_file_paths(input_directory, output_directory):
#     output_file_path = os.path.join(output_directory, 'filelist.txt')
#     with open(output_file_path, 'w') as file:
#         for root, dirs, files in os.walk(input_directory):
#             for file_name in files:
#                 file_path = os.path.join(root, file_name)
#                 file.write(file_path + '\n')

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python script.py <input_directory> <output_directory>")
#     else:
#         input_directory = sys.argv[1]
#         output_directory = sys.argv[2]
#         save_file_paths(input_directory, output_directory)
#         print(f'File paths have been saved to {os.path.join(output_directory, "filelist.txt")}')