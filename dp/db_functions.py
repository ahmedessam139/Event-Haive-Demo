import openpyxl
import datetime
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import gspread
import os


def check_and_update_attendance(code, excel_file):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook["Sheet"]

    # Get a list of QR code values from the first column
    codes = []
    for row in worksheet.iter_rows():
        codes.append(row[1].value)
        
################################
    # Check if the code is present in the list of QR code values
    if code not in codes:
        return "Not Found⛔"

    # Get the row number of the code
    row_num = codes.index(code) + 1

    # Check if the code has attended before
    if worksheet.cell(row=row_num, column=10).value == "Y":
        return "Already attended⛔"

    # Update the attendance
    if worksheet.cell(row=row_num, column=8).value != "Y":
        worksheet.cell(row=row_num, column=8, value="Y")
        worksheet.cell(row=row_num, column=10, value="Y")
        worksheet.cell(row=row_num, column=9, value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        worksheet.cell(row=row_num, column=11, value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


    if worksheet.cell(row=row_num, column=8).value == "Y":
        worksheet.cell(row=row_num, column=10, value="Y")
        worksheet.cell(row=row_num, column=11, value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Save the changes to the workbook
    workbook.save(excel_file)

    return "Valid✅"

def go_for_break(code, excel_file):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook["Sheet"]

    # Get a list of QR code values from the first column
    codes = []
    for row in worksheet.iter_rows():
        codes.append(row[1].value)

    # Check if the code is present in the list of QR code values
    if code not in codes:
        return "Not Found⛔"    

    # Get the row number of the code
    row_num = codes.index(code) + 1

    
    worksheet.cell(row=row_num, column=10, value=" ")
    workbook.save(excel_file)

    return "Enjoy your break✅"

def attendance_and_in_hall(excel_file):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook["Sheet"]

    sold_tickets_counter = 0
    attendance_counter = 0
    in_hall_counter = 0

    # Get a list of QR code values from the first column
    
    for row in worksheet.iter_rows():
        # print(type(row[3].value))
        #if type of row[3] is not NoneType
        if  row[3].value != None:
            sold_tickets_counter += 1
        if row[7].value == "Y":
            attendance_counter += 1
        if row[9].value == "Y":
            in_hall_counter += 1
    print(sold_tickets_counter-1, attendance_counter, in_hall_counter)
    return sold_tickets_counter-1, attendance_counter, in_hall_counter

def add_visitor(name, number, email, national_id):
    # Authenticate with Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('tickets-system-378204-ba8d2b4debfd.json', scope)
    client = gspread.authorize(creds)

    # Open the specified sheet
    sheet_name = "tickets"
    sheet = client.open(sheet_name).sheet1

    # Get a list of QR code values from the first column
    qr_codes = sheet.col_values(1)

    # Get the first empty cell in 5th column
    first_empty_cell = len(sheet.col_values(5)) + 1

    # Put parameters to sheet
    sheet.update_cell(first_empty_cell, 4, name)
    sheet.update_cell(first_empty_cell, 5, number)
    sheet.update_cell(first_empty_cell, 6, email)
    sheet.update_cell(first_empty_cell, 7, national_id)
    #get the cell number 3
    cell = sheet.cell(first_empty_cell, 3)
    return cell

# print(add_visitor("name", "number", "email", "national_id"))


def download_google_sheet_as_excel(sheet_name="tickets", folder_name="dp", file_name="tickets.xlsx"):
    # Set up the credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "dp/tickets-system-378204-ba8d2b4debfd.json",
        ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    )
    client = gspread.authorize(credentials)

    # Get the Google Sheet
    sheet = client.open(sheet_name).sheet1

    # Get the data from the Google Sheet
    data = sheet.get_all_values()

    # Create a new Excel workbook and worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Write the data to the Excel worksheet
    for row in data:
        worksheet.append(row)

    # Create the folder if it does not exist
    os.makedirs(folder_name, exist_ok=True)

    # Save the Excel workbook to the specified file path
    file_path = os.path.join(folder_name, file_name)
    workbook.save(file_path)


# upload_excel_to_google_sheet() 
# download_google_sheet_as_excel()
# add_user({'name': 'Ahmed Essam', 'mobile': '01146067319', 'email': 'ahmedtetohhh@gmail.com', 'nationalId': '30009131303116'})
# attendance_and_in_hall("dp/tickets.xlsx")