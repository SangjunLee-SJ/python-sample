import qrcode
import sys

def generate_qr_code(url, filename='qr_code.png'):
    qr = qrcode.QRCode(
        version=1,  # QR 코드 버전 (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정 레벨
        box_size=10,  # 각 박스 크기
        border=4,  # 테두리 크기
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    img.save(filename)
    print(f"QR code {filename} saved.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        generate_qr_code(url)
    else:
        print("python qr_code_generator.py URL")
