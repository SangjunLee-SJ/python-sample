# Please ensure that the service key file is named with the same name as the one in the code (service_account_credentials.json), in the same location.
# Please ensure that the Google Sheet name is the same as the one in the code (Working Timestamp).

import tkinter as tk
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def append_to_sheet(date, start_working, estimated_leaving_work, stop_working=""):
    # Set up credentials
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(current_directory, "service_account_credentials.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)

    client = gspread.authorize(creds)

    # Open the Google Sheet using its title
    sheet = client.open("Working Timestamp").sheet1
    
    if date and start_working and estimated_leaving_work:
        # If we have all three values, append a new row
        row = [date, start_working, estimated_leaving_work, stop_working]
        sheet.append_row(row)
        return row
    elif stop_working:
        # ... (this part stays the same)
        # Now, let's calculate the total hours worked:
        # If only stop_working is provided, update the last row
        last_row = len(sheet.get_all_values())
        start_time = datetime.strptime(sheet.cell(last_row, 2).value, '%H:%M:%S')
        end_time = datetime.strptime(stop_working, '%H:%M:%S')
        total_worked = end_time - start_time
        
        sheet.update_cell(last_row, 4, stop_working)  # 4 refers to the 'Stop_Working' column
        sheet.update_cell(last_row, 5, str(total_worked))  # Assuming 5th column is for total hours worked
        return [sheet.cell(last_row, 1).value, sheet.cell(last_row, 2).value, sheet.cell(last_row, 3).value, stop_working, str(total_worked)]

class WorkHoursApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Work Hours Calculator")
        
        # Button to start working
        self.start_btn = tk.Button(root, text="Start Working", command=self.start_working)
        self.start_btn.pack()
        
        # Button to stop working
        self.stop_btn = tk.Button(root, text="Stop Working", command=self.stop_working)
        self.stop_btn.pack()
        
        # Label to display total hours worked
        self.hours_label = tk.Label(root, text="Total hours worked: 00:00:00")
        self.hours_label.pack()
        
        # Listbox to display the history of working hours
        self.history_listbox = tk.Listbox(root)
        self.history_listbox.pack()
        
    def start_working(self):
        # Get the current timestamp
        current_time = datetime.now()
        date_str = current_time.strftime('%Y-%m-%d')
        time_str = current_time.strftime('%H:%M:%S')
        
        #Add or erase the lunch time +1
        estimated_leaving_time_str = (current_time + timedelta(hours=9)).strftime('%H:%M:%S')
        
        # Append to Google Sheets
        row_data = append_to_sheet(date_str, time_str, estimated_leaving_time_str)
        self.update_listbox(row_data)
        
    def stop_working(self):
        # Get the current timestamp
        current_time = datetime.now()
        time_str = current_time.strftime('%H:%M:%S')
        row_data = append_to_sheet("", "", "", time_str)
        self.update_listbox(row_data)
        # Update the label with the total hours worked
        self.hours_label.config(text=f"Total hours worked: {row_data[4]}")

    def update_listbox(self, row_data):
        # Convert the row data into a formatted string and insert into the listbox
        formatted_data = "\t".join(row_data)
        self.history_listbox.insert(tk.END, formatted_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkHoursApp(root)
    root.mainloop()
