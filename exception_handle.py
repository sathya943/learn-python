# Learning Exception Handling in Python
# Author Github: sathya943
# Date: 2025-07-06

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    return a / b

## Driver Code
print(divide(10, 0)) # ZeroDivisionError