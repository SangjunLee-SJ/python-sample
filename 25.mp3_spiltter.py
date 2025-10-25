import os
import subprocess # subprocess 모듈 추가

# --- 사용자 설정 영역 ---

# 1. 원본 MP3 파일 경로를 지정하세요.
source_mp3_path = "C:/a/video/8.mp3"

# 2. 분할된 파일들을 저장할 폴더 이름을 지정하세요.
output_folder = "C:/a/video/"

# 3. 분할할 구간을 목록으로 만드세요.
segments_to_split = [
    {
        "name": "1",
        "start": "0:00:01",
        "end": "1:00:00"
    },
    {
        "name": "2",
        "start": "1:00:01",
        "end": "2:00:00"
    },
    {
        "name": "3",
        "start": "2:00:01",
        "end": "3:00:02"
    }
]


# --- 코드 실행 영역 (FFmpeg를 사용하도록 변경됨) ---

def main():
    """ 메인 분할 로직 (FFmpeg 직접 호출 방식) """

    # 출력 폴더 생성
    os.makedirs(output_folder, exist_ok=True)
    
    # 원본 파일 존재 여부 확인
    if not os.path.exists(source_mp3_path):
        print(f"오류: 원본 파일 '{source_mp3_path}'를 찾을 수 없습니다.")
        return

    # 각 구간별로 파일 분할 시작
    for i, segment in enumerate(segments_to_split):
        name = segment["name"]
        start_time_str = segment["start"]
        end_time_str = segment["end"]
        
        print(f"\n[{i+1}/{len(segments_to_split)}] 작업 시작...")
        
        # 파일 이름에 포함될 수 없는 문자 제거 또는 변경
        safe_filename = "".join(c for c in name if c.isalnum() or c in (' ', '.', '_', '-')).rstrip()
        output_filename = f"{safe_filename}.mp3"
        output_path = os.path.join(output_folder, output_filename)

        print(f"  - 파일명: {output_filename}")
        print(f"  - 구간: {start_time_str} 부터 {end_time_str} 까지")
        print(f"  - 저장 경로: {output_path}")

        try:
            # FFmpeg 명령어 생성
            # -i: 입력 파일, -ss: 시작 시간, -to: 종료 시간
            # -c copy: 오디오를 다시 인코딩하지 않고 그대로 복사 (매우 빠름, 품질 저하 없음)
            command = [
                'ffmpeg',
                '-i', source_mp3_path,
                '-ss', start_time_str,
                '-to', end_time_str,
                '-c', 'copy',
                '-y', # 이미 파일이 존재하면 덮어쓰기
                output_path
            ]
            
            # FFmpeg 명령어 실행
            subprocess.run(command, check=True, capture_output=True, text=True)
            print("  - 저장 완료!")

        except FileNotFoundError:
            print("오류: ffmpeg가 설치되어 있지 않거나 PATH에 등록되지 않았습니다.")
            print("이전 답변을 참고하여 ffmpeg를 설치하고 환경 변수를 설정해주세요.")
            return
        except subprocess.CalledProcessError as e:
            print(f"  - 오류 발생: FFmpeg 실행 중 문제가 발생했습니다.")
            print(f"  - FFmpeg 오류 메시지: {e.stderr}")


    print("\n모든 작업이 완료되었습니다!")

if __name__ == "__main__":
    main()
