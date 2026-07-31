from openpyxl import Workbook # type: ignore
from datetime import date

workbook = Workbook()

sheet = workbook.active
sheet.title = "Employees"
sheet = workbook["Employees"]
workbook.create_sheet("Joining Date")

sheet1 = workbook["Joining Date"]

# Header
sheet.append(["ID", "Name", "Department", "Salary"])

# Data
sheet.append([101, "Boopathi", "IT", 50000])
sheet.append([102, "Ram", "HR", 45000])

current_date=date.today()

# header 
sheet1.append(["ID","joining Date","End Date"])

# Data
sheet1.append([101,date(2021,9,9),current_date ])
sheet1.append([102, date(2020,11,1), current_date])
workbook.save("Employee_mini.xlsx")

print("Excel Created Successfully")