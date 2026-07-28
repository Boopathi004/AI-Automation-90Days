# Day 04 Notes

## Inheritance

Inheritance is an OOP concept where one class acquires the properties and methods of another class.

Purpose:
- Code Reusability
- Easy Maintenance
- Better Program Structure

Syntax

class Parent:
    pass

class Child(Parent):
    pass

---

## Parent Class

Also called:
- Base Class
- Super Class

Contains common properties and methods.

---

## Child Class

Also called:
- Derived Class
- Sub Class

Inherits all accessible properties and methods from the Parent Class.

---

## Types of Inheritance

### 1. Single Inheritance

One Parent → One Child

Example

Animal
   ↓
Dog

---

### 2. Multilevel Inheritance

Parent → Child → Grandchild

Example

Animal
   ↓
Dog
   ↓
Puppy

---

### 3. Multiple Inheritance

One Child inherits from multiple Parents.

Example

Father + Mother
        ↓
      Child

---

### 4. Hierarchical Inheritance

One Parent has multiple Child classes.

Example

Vehicle
 /    \
Car   Bike

---

## Method Overriding

The Child Class provides its own implementation of a Parent Class method.

Example

Parent:
display()

Child:
display()

The Child method replaces the Parent method.

---

## super()

super() is used to access the Parent Class constructor or methods.

Example

super().__init__()

super().display()

Advantages

- Reuse Parent Code
- Avoid Duplicate Code
- Better Readability

---

## Advantages of Inheritance

- Code Reusability
- Less Code
- Easy Maintenance
- Better Organization
- Faster Development

---

## Real-World Examples

Person → Student

Employee → Manager

Vehicle → Car

Animal → Dog

Account → SavingsAccount

Doctor → Person

---

## Keywords

Inheritance

Parent Class

Child Class

Base Class

Derived Class

super()

Method Overriding

Code Reusability

---

## Interview Questions

Q. What is Inheritance?

Inheritance allows one class to acquire the properties and methods of another class.

---

Q. Why is Inheritance used?

To reuse existing code and reduce duplication.

---

Q. What is a Parent Class?

A class that provides common properties and methods.

---

Q. What is a Child Class?

A class that inherits from a Parent Class.

---

Q. What is Method Overriding?

A Child Class replaces the implementation of a Parent Class method.

---

Q. What is super()?

super() calls methods or constructors from the Parent Class.

---

## Today's Mini Projects

✔ School Management System

✔ Employee Management System

✔ Vehicle Management System

✔ Bank Management System

✔ Company Management System

✔ Hospital Management System

---

## Today's Learning Summary

✔ Inheritance

✔ Parent & Child Classes

✔ Single Inheritance

✔ Multilevel Inheritance

✔ Multiple Inheritance

✔ Hierarchical Inheritance

✔ Method Overriding

✔ super()

✔ Real-World Projects

---

## Progress

✅ Day 04 Completed