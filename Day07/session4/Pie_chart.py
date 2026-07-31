from openpyxl import Workbook #type:ignore
from openpyxl.chart import PieChart, Reference #type:ignore

wb = Workbook()

sheet = wb.active

sheet.append(["Department", "Employees"])

sheet.append(["IT", 10])
sheet.append(["HR", 5])
sheet.append(["Sales", 7])
sheet.append(["Admin", 4])

data = Reference(sheet,
                 min_col=2,
                 min_row=1,
                 max_row=5)

labels = Reference(sheet,
                   min_col=1,
                   min_row=2,
                   max_row=5)

chart = PieChart()

chart.title = "Department Employees"

chart.add_data(data, titles_from_data=True)

chart.set_categories(labels)

sheet.add_chart(chart, "D2")

wb.save("pie_chart.xlsx")