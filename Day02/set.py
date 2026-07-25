#exercise 1: creating a set
colors = {"Red", "Green", "Blue", "Yellow"}
print(colors)

#exercise 2: adding an element to a set
colors.add("Orange")
print(colors)

#exercise 3: removing an element from a set
colors.remove("Green")
print(colors)

#exercise 4: checking if an element is in a set
if "Blue" in colors:
    print("Blue is in the set")

#exercise 5: union of two sets
A = {10,20,30}
B = {30,40,50}
C = A.union(B)
print(C)

#exercise 6: intersection of two sets
D=(A & B)
print(D)

#exercise 7: difference of two sets
E = (A-B)
print(E)

#exercise 8: removing duplicates from a list using set
marks = [90,95,95,90,88,70,88,99]
unique_marks = set(marks)
print(unique_marks)



#Mini Project: creating a set of students and performing operations
students = {
    "Boopathi",
    "Arun",
    "Rohan",
    "Boopathi",
    "Vijay",
    "Arun"
}

unique_stud=set(students)
added_stud=unique_stud.add("Kumar")
removed_stud=unique_stud.remove("Rohan")
print("Unique Students:", unique_stud)
