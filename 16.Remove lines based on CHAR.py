def remove_lines_from_file(file_path, substring):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = [line for line in lines if substring not in line]

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    substring = "\RECORDS"  # 이 문자열을 포함하는 줄을 삭제합니다.
    remove_lines_from_file(file_path, substring)
    print(f"All lines containing '{substring}' have been removed from {file_path}.")
