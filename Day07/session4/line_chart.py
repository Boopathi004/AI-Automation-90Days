from openpyxl import Workbook #type:ignore
from openpyxl.chart import LineChart, Reference #type:ignore

wb = Workbook()

sheet = wb.active

sheet.append(["Month", "Sales"])

sheet.append(["Jan", 25000])
sheet.append(["Feb", 32000])
sheet.append(["Mar", 29000])
sheet.append(["Apr", 41000])
sheet.append(["May", 39000])

data = Reference(sheet,
                 min_col=2,
                 min_row=1,
                 max_row=6)

categories = Reference(sheet,
                       min_col=1,
                       min_row=2,
                       max_row=6)

chart = LineChart()

chart.title = "Monthly Sales"

chart.add_data(data, titles_from_data=True)

chart.set_categories(categories)

sheet.add_chart(chart, "D2")

wb.save("line_chart.xlsx")