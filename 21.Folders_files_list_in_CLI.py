import os

def print_directory_structure(root_dir, indent=""):
    # 현재 디렉토리의 모든 항목을 나열
    items = sorted(os.listdir(root_dir))
    for index, item in enumerate(items):
        item_path = os.path.join(root_dir, item)
        # 마지막 항목인지 확인하여 연결선 모양 결정
        if index == len(items) - 1:
            connector = "└── "
            new_indent = indent + "    "
        else:
            connector = "├── "
            new_indent = indent + "│   "
        
        # 디렉토리인지 파일인지 확인
        if os.path.isdir(item_path):
            print(f"{indent}{connector}{item}/")
            # 재귀 호출하여 하위 디렉토리 탐색
            print_directory_structure(item_path, new_indent)
        else:
            print(f"{indent}{connector}{item}")

if __name__ == "__main__":
    # 탐색할 최상위 디렉토리 경로 설정
    # 예: 'C:/SOP_Files/a' 또는 './a'
    root_directory = input("디렉토리 경로를 입력하세요: ").strip()

    if not os.path.exists(root_directory):
        print("지정한 디렉토리가 존재하지 않습니다.")
    elif not os.path.isdir(root_directory):
        print("지정한 경로는 디렉토리가 아닙니다.")
    else:
        print(f"\n디렉토리 구조: {root_directory}\n")
        print_directory_structure(root_directory)
