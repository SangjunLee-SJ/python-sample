# https://digi.bib.uni-mannheim.de/tesseract/
# tesseract-ocr-w64-setup-5.3.0.20221222.exe
# https://github.com/tesseract-ocr/tessdata/blob/main/kor.traineddata (C:/Program Files/Tesseract-OCR/tessdata)

# C:/Program Files/Tesseract-OCR 설치 완료 후 경로 설정

# pip install pytesseract



# import pytesseract
# from PIL import Image
# import os

# # Tesseract 경로 설정 (Tesseract 설치 경로에 맞게 변경)
# pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# # 폴더 내의 모든 이미지 파일에서 텍스트를 추출하고 하나의 텍스트 파일로 모으는 함수
# def extract_text_to_file(input_folder, output_file):
#     # 결과를 담을 문자열 초기화
#     combined_text = ""
    
#     # 지정된 폴더 내의 모든 파일에 대해 반복
#     for filename in os.listdir(input_folder):
#         # 이미지 파일인 경우에만 처리
#         if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
#             # 이미지 파일의 경로
#             image_path = os.path.join(input_folder, filename)
#             # 이미지 파일 로드
#             image = Image.open(image_path)
#             # OCR을 사용하여 이미지에서 텍스트 추출
#             text = pytesseract.image_to_string(image, lang='kor+eng')
#             # 파일명과 함께 추출된 텍스트를 추가
#             combined_text += f"--- {filename} ---/n{text}/n/n"
    
#     # 추출된 텍스트를 출력 파일에 저장
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write(combined_text)

# # 사용 예시 (실제 경로로 변경)
# input_folder = 'C:/Users/user/Downloads/b'
# output_file = 'C:/Users/user/Downloads/b/text_file.txt'
# extract_text_to_file(input_folder, output_file)



# 변형하면 아래처럼 작성도 가능.


import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os
import re

# Tesseract 경로 설정 (Tesseract 설치 경로에 맞게 변경)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# 이미지 전처리를 위한 함수
def preprocess_image(image_path):
    image = Image.open(image_path)
    # 명암 대비를 개선
    image = ImageEnhance.Contrast(image).enhance(2)
    # 이미지를 흑백으로 변환
    image = image.convert('L')
    # 이미지의 날카로움을 개선
    image = image.filter(ImageFilter.SHARPEN)
    # 잡음 제거를 위해 이미지 이진화
    image = image.point(lambda x: 0 if x < 140 else 255)
    return image

# OCR 후처리를 위한 함수
def postprocess_text(text):
    # 불필요한 공백 및 줄바꿈 문자 제거
    text = re.sub(r'/n+', '/n', text).strip()
    # OCR이 잘못 인식하는 특정 패턴 수정 (예: 소 프 트 웨 어 -> 소프트웨어)
    text = re.sub(r'소 프 트 웨 어', '소프트웨어', text)
    return text

# 폴더 내의 모든 이미지 파일에서 텍스트를 추출하고 하나의 텍스트 파일로 모으는 함수
def extract_text_to_file(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                image_path = os.path.join(input_folder, filename)
                # 이미지 전처리
                preprocessed_image = preprocess_image(image_path)
                # OCR을 사용하여 이미지에서 텍스트 추출
                text = pytesseract.image_to_string(preprocessed_image, lang='kor+eng')
                # 텍스트 후처리
                processed_text = postprocess_text(text)
                # 파일명과 함께 추출된 텍스트를 파일에 쓰기
                file.write(f"--- {filename} ---/n{processed_text}/n/n")

# 사용 예시 (실제 경로로 변경)
input_folder = 'C:/Users/user/Downloads/b'
output_file = 'C:/Users/user/Downloads/b/text_file.txt'
extract_text_to_file(input_folder, output_file)
