import os

def merge_txt_files_with_numbers(folder_path, output_file):
    try:
        # 폴더 내 txt 파일 가져오기
        txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        txt_files.sort()  # 파일 이름 순 정렬 (필요 시 정렬 기준 수정 가능)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for idx, txt_file in enumerate(txt_files, start=1):
                file_path = os.path.join(folder_path, txt_file)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # 파일 번호 추가
                    outfile.write(f"{idx}\n")
                    outfile.write(infile.read())
                    outfile.write('\n')  # 파일 간 줄바꿈 추가
        print(f"모든 TXT 파일이 '{output_file}'로 성공적으로 합쳐졌습니다!")
    except Exception as e:
        print(f"오류 발생: {e}")


# 예제 실행
folder_path = "C:/a/video/output"  # .txt 파일들이 있는 폴더 경로
output_file = "C:/a/video/output/merged_output.txt"  # 출력 파일 경로
merge_txt_files_with_numbers(folder_path, output_file)
