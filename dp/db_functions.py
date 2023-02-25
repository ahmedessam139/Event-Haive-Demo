import openpyxl
import datetime
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import gspread
import os


def add_visitor(name, number, email, national_id):
    # Authenticate with Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('tickets-system-378204-ba8d2b4debfd.json', scope)
    client = gspread.authorize(creds)

    # Open the specified sheet
    sheet_name = "tickets"
    sheet = client.open(sheet_name).sheet1

    # Get a list of QR code values from the first column

    # Get the first empty cell in 5th column
    mobile_numbers = sheet.col_values(5)
    for i, numberr in enumerate(mobile_numbers):
        if numberr == None or numberr == "":
            first_empty_cell = i+1
            break 


    # Put parameters to sheet
    sheet.update_cell(first_empty_cell, 4, name)
    sheet.update_cell(first_empty_cell, 5, number)
    sheet.update_cell(first_empty_cell, 6, email)
    sheet.update_cell(first_empty_cell, 7, national_id)
    #get the cell number 3
    cell = sheet.cell(first_empty_cell, 3)
    return cell

# print(add_visitor("name", "number", "email", "national_id"))

def add_visitor_by_number(number,id):
    # Authenticate with Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('tickets-system-378204-ba8d2b4debfd.json', scope)
    client = gspread.authorize(creds)

    # Open the specified sheet
    sheet_name = "tickets"
    sheet = client.open(sheet_name).sheet1


    # Get the row number byid from first colomn
    ids = sheet.col_values(1)
    for i, idd in enumerate(ids):
        if idd == id:
            sheet.update_cell(i+1, 5, number)
            break
    
    cell = sheet.cell(i+1, 3)
    return cell
    

# print(add_visitor_by_number("01234","10"))

# upload_excel_to_google_sheet() 
# download_google_sheet_as_excel()
# add_user({'name': 'Ahmed Essam', 'mobile': '01146067319', 'email': 'ahmedtetohhh@gmail.com', 'nationalId': '30009131303116'})
# attendance_and_in_hall("dp/tickets.xlsx")