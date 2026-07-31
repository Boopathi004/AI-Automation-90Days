from openpyxl import load_workbook #type:ignore

workbook = load_workbook("Employee_mini.xlsx")

sheet = workbook["Employees"]

sheet["D2"] = 65000

workbook.save("Employee_mini.xlsx")

print("Salary Updated Successfully")
print("Salary :", sheet["D3"].value)
print("Salary :", sheet["D2"].value)