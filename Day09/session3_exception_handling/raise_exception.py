age = int(input("Enter Age: "))

if age < 18:
    raise Exception("You are not eligible to vote.")

print("Eligible")