'''
def get_number():
    return[1,2,3,4,5,6]

def numbers():
    for i in range(1, 6):
        yield i
        print(f"Generator Numbers : ",i)
    

print(f"all Numbers : ",get_number())
print(list(numbers()))'''

def employees_generator():
    for employee in range(101, 106):
        yield employee

for employee_id in employees_generator():
    print(f"Generator Employee: {employee_id}")