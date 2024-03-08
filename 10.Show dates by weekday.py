from datetime import datetime, timedelta

def get_week_number(date):
    return date.isocalendar()[1]

def display_weeks(start_date, end_date):
    current_date = start_date
    week_number = 1

    while current_date <= end_date:
        print(f"{week_number}주차-{current_date.strftime('%Y.%m.%d')}")
        current_date += timedelta(days=7)
        week_number += 1

# Start date와 End date를 입력 받기
start_date_str = input("Start date를 입력하세요 (예: 2024.03.08): ")
end_date_str = input("End date를 입력하세요 (예: 2024.06.14): ")

# 문자열을 datetime 객체로 변환
start_date = datetime.strptime(start_date_str, "%Y.%m.%d")
end_date = datetime.strptime(end_date_str, "%Y.%m.%d")

# 주차 텍스트 표시
display_weeks(start_date, end_date)
