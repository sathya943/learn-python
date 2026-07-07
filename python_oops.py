# Learn Python Object Oriented Programming Concepts Here.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Cannot divide by zero"
    
    def display(self):
        print(f"Addition: {self.add()}")
        print(f"Subtraction: {self.subtract()}")
        print(f"Multiplication: {self.multiply()}")
        print(f"Division: {self.divide()}")

# Driver Code
# person1 = Person("Satya", 22)
# person1.display()

calculator1 = Calculator(10, 5)
calculator1.display()