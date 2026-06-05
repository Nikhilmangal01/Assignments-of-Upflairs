# class Employee:
#     def __init__(self, name, id, salary):
#         self.name = emp_name
#         self.id = emp_id
#         self.salary = salary

#     def display(self):
#         print("Employee Name :", self.name)
#         print("Employee ID   :", self.id)
#         print("Salary        :", self.salary)
#         print()


# emp1 = Employee("Nikhil", 101, 50000)
# emp2 = Employee("Kushagra", 102, 60000)
# emp3 = Employee("Om", 103, 55000)

# print("----- Employee Details -----")
# emp1.display()
# emp2.display()
# emp3.display()


# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         return a / b


# calc = Calculator()

# print("----- Calculator Operations -----")
# print("Addition       :", calc.add(10, 5))
# print("Subtraction    :", calc.subtract(10, 5))
# print("Multiplication :", calc.multiply(10, 5))
# print("Division       :", calc.divide(10, 5))
# print()


# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def display(self):
#         print("Title  :", self.title)
#         print("Author :", self.author)
#         print("Price  :", self.price)
#         print()


# book1 = Book("Python Programming", "OM MUDGAL", 499)

# print("----- Book Details -----")
# book1.display()


# class Vehicle:
#     def display(self):
#         print("This is a Vehicle")


# class Car(Vehicle):
#     def show(self):
#         super().display()
#         print("This is a Car")


# car = Car()

# print("----- Inheritance Example -----")
# car.show()
# print()


# import re

# text = "Python123Assignment456"

# digits = re.findall(r'\d+', text)

# print("----- Regex Output -----")
# print("Digits found:", digits)