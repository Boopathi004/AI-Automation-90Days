from openpyxl import Workbook #type:ignore

wb = Workbook()
sheet = wb.active

sheet.freeze_panes = "A2"

wb.save("freeze_demo.xlsx")