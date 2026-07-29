from datetime import datetime

birth_year = int(input("Enter Birth Year: "))

current_year = datetime.now().year

age = current_year - birth_year

print("Your Age is:", age)