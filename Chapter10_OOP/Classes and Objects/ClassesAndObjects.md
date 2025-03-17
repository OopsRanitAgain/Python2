# OOP in Python

## Introduction
In Python, **classes** and **objects** are fundamental concepts of **Object-Oriented Programming (OOP)**. A class is a blueprint for creating objects, and an object is an instance of a class.

---
## 1. What is a Class?
A **class** is a user-defined data structure that contains attributes (variables) and methods (functions) to operate on the data.

### Syntax of a Class:
```python
class ClassName:
    # Constructor (initializer)
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1  # Instance Variable
        self.attribute2 = attribute2

    # Method
    def method_name(self):
        return f"Attribute 1: {self.attribute1}, Attribute 2: {self.attribute2}"
```

---
## 2. What is an Object?
An **object** is an instance of a class. When a class is defined, no memory is allocated until an object is created.

### Creating an Object:
```python
obj = ClassName("Value1", "Value2")
print(obj.method_name())
```

---
## 3. Constructors (`__init__` Method)
The **constructor** is a special method called automatically when an object is created. In Python, it is defined using `__init__`.

### Example:
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        return f"Car: {self.brand} {self.model}"

car1 = Car("Toyota", "Corolla")
print(car1.show_details())
```

---
## 4. Instance and Class Variables
- **Instance Variables**: Unique to each instance of a class.
- **Class Variables**: Shared among all instances.

### Example:
```python
class Student:
    school_name = "XYZ High School"  # Class Variable

    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age

s1 = Student("Alice", 15)
s2 = Student("Bob", 16)

print(s1.school_name)  # XYZ High School
print(s2.school_name)  # XYZ High School
```

---
## 5. Methods in a Class
1. **Instance Methods**: Operate on instance variables.
2. **Class Methods (`@classmethod`)**: Operate on class variables.
3. **Static Methods (`@staticmethod`)**: Independent of class/instance variables.

### Example:
```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

print(MathOperations.add(5, 3))  # 8
```

---
## 6. Inheritance
**Inheritance** allows a class (child class) to inherit methods and attributes from another class (parent class).

### Example:
```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

d = Dog()
print(d.speak())  # Dog barks
```

---
## 7. Encapsulation
Encapsulation restricts direct access to variables and methods.
- **Public (`self.var`)**: Accessible anywhere.
- **Private (`self.__var`)**: Accessible only within the class.

### Example:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Variable

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())  # 1000
```

---
## 8. Polymorphism
Polymorphism allows different classes to have methods with the same name but different behavior.

### Example:
```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak())
```

---
## Conclusion
Classes and objects form the foundation of **Object-Oriented Programming (OOP)** in Python. By using encapsulation, inheritance, and polymorphism, we can create efficient, reusable, and modular code.
