
#imporing the module 

import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))

#Notes: 

'''Import specific function 

from calculator import add

print(add(100, 50))
'''
'''import with an multiple function 

from calculator import add, subtract
'''
'''Import with an alias

import calculator as calc

print(calc.add(5, 5)) 
'''
'''
utils/
│
├── __init__.py
├── calculator.py
└── converter.py

'''
'''import from package 

from utils.calculator import add

print(add(10, 20))
'''