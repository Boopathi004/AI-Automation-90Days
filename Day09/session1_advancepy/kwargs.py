def employee_details(**details):

    for key, value in details.items():
        print(f"{key}: {value}")

employee_details(
    Name="Boopathi",
    Department="IT",
    Salary=50000
)