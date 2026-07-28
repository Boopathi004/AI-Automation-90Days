# 📘 Day 04 Notes

---

# 1. Inheritance

## Definition

Inheritance is an Object-Oriented Programming concept where one class inherits the properties and methods of another class.

Purpose

- Code Reusability
- Easy Maintenance
- Better Program Structure

---

## Types of Inheritance

### Single Inheritance

One Parent → One Child

### Multilevel Inheritance

Parent → Child → Grandchild

### Multiple Inheritance

Multiple Parents → One Child

### Hierarchical Inheritance

One Parent → Multiple Children

---

## Method Overriding

A Child Class provides its own implementation of a Parent Class method.

---

## super()

Used to access Parent Class constructors and methods.

Example

super().__init__()

super().display()

---

# 2. Encapsulation

## Definition

Encapsulation is the process of combining data and methods into a single class while protecting data from direct access.

---

## Access Modifiers

### Public

Accessible from anywhere.

Example

self.name

---

### Protected

Uses one underscore.

Example

self._salary

---

### Private

Uses double underscore.

Example

self.__balance

---

## Getter Method

Returns private data.

Example

get_balance()

---

## Setter Method

Updates private data safely.

Example

set_balance()

---

## Advantages

- Data Hiding
- Better Security
- Easy Maintenance
- Controlled Access

---

# 3. Polymorphism

## Definition

Polymorphism means "Many Forms."

The same method behaves differently depending on the object.

---

## Types

### Method Overriding

Child class changes Parent method.

---

### Duck Typing

Python checks behaviour instead of object type.

---

### Operator Overloading

Operators behave differently for different objects.

Example

+

works for

- Numbers
- Strings
- Lists

---

## Advantages

- Flexibility
- Reusability
- Clean Code
- Better Design

---

# 4. Exception Handling

## Definition

Exception Handling prevents program crashes caused by runtime errors.

---

## Keywords

### try

Contains risky code.

---

### except

Handles errors.

---

### else

Runs if no exception occurs.

---

### finally

Always executes.

---

### raise

Creates an exception manually.

---

### Custom Exception

User-defined exception created using the Exception class.

Example

class InvalidAgeError(Exception):
    pass

---

## Common Exceptions

- ZeroDivisionError
- ValueError
- TypeError
- FileNotFoundError
- IndexError
- KeyError

---

# Mini Projects

- School Management
- Employee Management
- Vehicle Management
- Bank Management
- Company Management
- Hospital Management
- Bank Account
- Employee Salary
- Payment System
- Notification System
- ATM Withdrawal
- Login Validation
- Calculator
- Student Marks Validation

---

# Interview Questions

### What is Inheritance?

Inheritance allows one class to inherit properties and methods from another class.

---

### What is Encapsulation?

Encapsulation protects data by controlling access through methods.

---

### What is Polymorphism?

Polymorphism allows the same method to perform different actions based on the object.

---

### What is Exception Handling?

Exception Handling prevents applications from crashing when runtime errors occur.

---

### What is super()?

super() calls Parent Class methods or constructors.

---

### What is Method Overriding?

A Child Class replaces a Parent Class method with its own implementation.

---

# Day 4 Summary

✅ Inheritance

✅ Advanced Inheritance

✅ Encapsulation

✅ Polymorphism

✅ Exception Handling

✅ 14+ Mini Projects

---

# Status

🎉 Day 04 Successfully Completed