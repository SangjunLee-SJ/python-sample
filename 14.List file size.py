import os
import math  # 필요한 모듈을 올바른 위치에 가져옵니다.

def convert_size(size_bytes):
    """ Convert the size from bytes to a more readable format (B, KB, MB, GB) """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def get_folder_size(path):
    """ Calculate total size of all files within the folder """
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            if not os.path.islink(filepath):
                total_size += os.path.getsize(filepath)
    return total_size

def list_directory_contents(path):
    """ List the contents of the directory, showing size of files and folders """
    if not os.path.exists(path):
        print(f"The path {path} does not exist.")
        return

    print(f"Contents of {path}:")
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                size = os.path.getsize(entry)
                print(f"File: {entry.name} - {convert_size(size)}")
            elif entry.is_dir():
                folder_size = get_folder_size(entry.path)
                print(f"Directory: {entry.name} - {convert_size(folder_size)}")

def main():
    while True:
        directory_path = input("Enter the directory path (or 'exit' to quit): ")
        if directory_path.lower() == 'exit':
            break
        list_directory_contents(directory_path)

if __name__ == "__main__":
    main()
