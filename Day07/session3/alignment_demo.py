from openpyxl import Workbook #type:ignore
from openpyxl.styles import Alignment #type:ignore

wb = Workbook()
sheet = wb.active

sheet["A1"] = "Employee Report"

sheet["A1"].alignment = Alignment(
    horizontal="center",
    vertical="center"
)

wb.save("alignment_demo.xlsx")