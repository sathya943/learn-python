# Learn Python Object Oriented Programming Concepts Here.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Driver Code
person1 = Person("Satya", 22)
person1.display()