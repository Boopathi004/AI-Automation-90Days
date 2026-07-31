from openpyxl import Workbook  # type: ignore[import]

# Create workbook
workbook = Workbook()

# Get active worksheet
sheet = workbook.active

# Rename sheet
sheet.title = "Employees"

# Save workbook
workbook.save("employees.xlsx")

print("Excel file created successfully!")