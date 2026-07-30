# Getting The file information from the system 

from pathlib import Path
import sys
file_name=input("enter the filename :")

file= Path(file_name)

print("file name:",file.name)
print("\n file stem:",file.stem)
print("\n file extenction:",file.suffix)

if file.exists():
    print ("\n Existing :yes")
else:
    print("\n Existing : no")

if file.exists()== False:
    print("\n do you want to create a file(y/n)?")
    user=input()
    if user=="y":
        file=Path(file_name)
        file.touch(exist_ok=True)
        print("file created ")
    
print("\n file path:",file.resolve())
print("\n size:",file.stat().st_size) 
