import os

filename="currentdir.py"

if os.path.exists(filename):
    print("file is exsist")
else:
    print("file not found ")