from openpyxl import Workbook #type:ignore
from openpyxl.styles import Border, Side #type:ignore

wb = Workbook()
sheet = wb.active

sheet["A1"] = "Boopathi"

border = Border(
    left=Side(style="thick"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin")
)

sheet["A1"].border = border

wb.save("border_demo.xlsx")