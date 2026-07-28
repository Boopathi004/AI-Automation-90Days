#Exception Handling
name=input("enter your name ") 

try:
    Mark=int(input("enter Your Mark"))
    if Mark<0 or Mark>=100:
        raise Exception("Enter the valid mark ")
    print("name",name)
    print("mark",Mark)
except Exception as e:
    print(e)  
if Mark>=90:
    print("grade A")
elif Mark>=80:
    print("grade B")
elif Mark>60:
    print("grade C")
else:
    print("fail")

