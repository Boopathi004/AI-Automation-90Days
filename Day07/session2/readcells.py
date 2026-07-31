from openpyxl import load_workbook #type:ignore 

workbook = load_workbook("Employee_mini.xlsx")

sheet = workbook["Employees"]

print("Employee ID :", sheet["A2"].value)
print("Employee Name :", sheet["B2"].value)
print("Department :", sheet["C2"].value)
print("Salary :", sheet["D2"].value)