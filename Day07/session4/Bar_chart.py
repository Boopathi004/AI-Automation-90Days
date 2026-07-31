from openpyxl import Workbook #type:ignore
from openpyxl.chart import BarChart, Reference #type:ignore

wb = Workbook()
sheet = wb.active

sheet.append(["Department", "Salary"])

sheet.append(["IT", 80000])
sheet.append(["HR", 45000])
sheet.append(["Sales", 55000])
sheet.append(["Admin", 35000])

data = Reference(sheet,
                 min_col=2,
                 min_row=1,
                 max_row=5)

categories = Reference(sheet,
                       min_col=1,
                       min_row=2,
                       max_row=5)

chart = BarChart()

chart.title = "Department Salary"

chart.add_data(data, titles_from_data=True)

chart.set_categories(categories)

sheet.add_chart(chart, "D2")

wb.save("bar_chart.xlsx")

print("Bar Chart Created")