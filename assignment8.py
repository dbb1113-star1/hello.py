# assignment8.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

# Get user input and convert to float
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call each function and display the results
print("\n--- Calculation Results ---")
print(f"Addition ({num1} + {num2}): {add(num1, num2)}")
print(f"Subtraction ({num1} - {num2}): {subtract(num1, num2)}")
print(f"Multiplication ({num1} * {num2}): {multiply(num1, num2)}")
print(f"Division ({num1} / {num2}): {divide(num1, num2)}")