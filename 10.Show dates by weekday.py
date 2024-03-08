from datetime import datetime, timedelta

def get_week_number(date):
    return date.isocalendar()[1]

def display_weeks(start_date, end_date):
    current_date = start_date
    week_number = 1

    while current_date <= end_date:
        print(f"{week_number} Week-{current_date.strftime('%Y.%m.%d')}")
        current_date += timedelta(days=7)
        week_number += 1

start_date_str = input("Input Start date (ex: 2024.03.08): ")
end_date_str = input("Input End date (ex: 2024.06.14): ")

start_date = datetime.strptime(start_date_str, "%Y.%m.%d")
end_date = datetime.strptime(end_date_str, "%Y.%m.%d")

display_weeks(start_date, end_date)
