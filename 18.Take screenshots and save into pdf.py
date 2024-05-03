from pynput import keyboard, mouse
from PIL import ImageGrab
from fpdf import FPDF
import os

# 좌표 설정 변수
left_top = None
right_bottom = None
image_paths = []
orientation = "L"  #('P' for portrait, 'L' for landscape)

def on_press(key):
    global left_top, right_bottom

    try:
        if key.char == '-':
            # 현재 마우스 위치를 좌표로 사용
            x, y = mouse.Controller().position
            if not left_top:
                left_top = (x, y)
                print(f"Left top corner set at: {left_top}")
            elif not right_bottom:
                right_bottom = (x, y)
                print(f"Right bottom corner set at: {right_bottom}")
        elif key.char == '=':
            # 스크린샷 찍기
            if left_top and right_bottom:
                bbox = (*left_top, *right_bottom)
                screenshot = ImageGrab.grab(bbox)
                img_path = f'temp_img_{len(image_paths)}.png'
                screenshot.save(img_path)
                image_paths.append(img_path)
                print(f"Screenshot taken and saved at {img_path}. Total stored: {len(image_paths)}")
    except AttributeError:
        pass

def on_release(key):
    # Enter 키를 누르면 모든 이미지를 PDF로 저장
    if key == keyboard.Key.enter:
        print("Saving PDF...")
        save_pdf(image_paths, orientation)
        return False  # 리스너 종료

def save_pdf(image_paths, orientation):
    # 사용자에게 문서 방향 선택 요청
    orientation = orientation


    pdf = FPDF(orientation, 'mm', 'A4')
    full_path = "C:/Users/user/Desktop/output.pdf"

    for path in image_paths:
        pdf.add_page()
        if orientation == 'P':
            pdf.image(path, x=10, y=10, w=180)  # 세로 페이지에 맞게 이미지 추가
        else:
            pdf.image(path, x=10, y=10, w=260)  # 가로 페이지에 맞게 이미지 추가
        os.remove(path)  # PDF에 추가 후 이미지 파일 삭제

    pdf.output(full_path, 'F')
    print(f"PDF saved at {full_path}")

# 키보드 리스너 실행
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
