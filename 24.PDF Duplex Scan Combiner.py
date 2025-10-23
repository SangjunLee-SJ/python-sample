import sys
from pypdf import PdfReader, PdfWriter

# 1. 1st Odd pages (page 1, 3, 5, 7...)
FRONT_PAGES_FILE = "C:/a/scan/p1.pdf" 
# 2. 2st Even pages (page ...8, 6, 4, 2)
BACK_PAGES_FILE = "C:/a/scan/p2.pdf"
# 3. Save pdf name
OUTPUT_FILENAME = "C:/a/scan/combine.pdf"


def combine_two_files(front_path, back_path, output_path):
    try:
        reader_front = PdfReader(front_path)
        reader_back = PdfReader(back_path)
    except FileNotFoundError as e:
        print(f"오류: 파일을 찾을 수 없습니다. {e.filename}")
        print("FRONT_PAGES_FILE 또는 BACK_PAGES_FILE 이름을 확인하세요.")
        return
    except Exception as e:
        print(f"PDF를 읽는 중 오류가 발생했습니다: {e}")
        return

    writer = PdfWriter()

    num_front = len(reader_front.pages)
    num_back = len(reader_back.pages)

    print(f"앞면 파일 ('{front_path}'): {num_front} 페이지")
    print(f"뒷면 파일 ('{back_path}'): {num_back} 페이지")

    # 총 페이지가 홀수인지 짝수인지 확인
    if num_front != num_back and num_front != num_back + 1:
        print("\n경고: 앞면과 뒷면 페이지 수가 맞지 않습니다.")
        print(f"앞면: {num_front}장, 뒷면: {num_back}장")
        print("정확히 정렬되지 않을 수 있습니다. 계속 진행합니다...")

    # 짝수 페이지 수(뒷면)만큼 반복합니다.
    for i in range(num_back):
        # 1. 앞면 파일에서 페이지를 순서대로 가져옵니다. (0, 1, 2...)
        writer.add_page(reader_front.pages[i])
        
        # 2. 뒷면 파일에서 페이지를 *역순*으로 가져옵니다. (N-1, N-2, N-3...)
        writer.add_page(reader_back.pages[num_back - 1 - i])

    # 만약 앞면 페이지가 뒷면 페이지보다 많으면 (총 페이지가 홀수)
    if num_front > num_back:
        # 앞면 파일의 마지막 페이지를 추가합니다.
        writer.add_page(reader_front.pages[num_front - 1])
        print("총 페이지가 홀수이므로, 마지막 앞면 페이지를 추가했습니다.")

    # 결과 파일 저장
    try:
        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"\n성공! '{output_path}' 파일로 저장되었습니다.")
    except Exception as e:
        print(f"파일을 저장하는 중 오류가 발생했습니다: {e}")

# 스크립트 실행
if __name__ == "__main__":
    combine_two_files(FRONT_PAGES_FILE, BACK_PAGES_FILE, OUTPUT_FILENAME)
