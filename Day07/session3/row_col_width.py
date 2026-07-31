from openpyxl import Workbook #type:ignore

wb = Workbook()
sheet = wb.active

sheet.column_dimensions["A"].width = 30

sheet.row_dimensions[1].height = 30

sheet["A1"] = "Employee"

wb.save("size_demo.xlsx")