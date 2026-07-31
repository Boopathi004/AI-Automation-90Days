from openpyxl import Workbook #type:ignore

wb = Workbook()
sheet = wb.active

sheet.merge_cells("A1:D1")

sheet["A1"] = "ABC Company Pvt Ltd"

wb.save("merge_demo.xlsx")