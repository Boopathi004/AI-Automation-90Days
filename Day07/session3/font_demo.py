from openpyxl import Workbook #type:ignore 
from openpyxl.styles import Font #type:ignore 

wb = Workbook()
sheet = wb.active

sheet["A1"] = "Employees"

sheet["A1"].font = Font(
    bold=True,
    italic=True,
    size=18,
    color="FF0000"
)

wb.save("font_demo.xlsx")

print("Font Formatting Completed")