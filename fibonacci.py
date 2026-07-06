# Python programming for fibonacci series using functions.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Driver Code
print(fibonacci(9))