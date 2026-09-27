# Step 1: Prompt the user for three numbers
num1 = input("Enter the first number (num1): ")
num2 = input("Enter the second number (num2): ")
num3 = input("Enter the third number (num3): ")

# Step 2: Print the initial values and data types (which will be 'str')
print(f"The value of num1 is {num1}, and it is of the type {type(num1)}.")
print(f"The value of num2 is {num2}, and it is of the type {type(num2)}.")
print(f"The value of num3 is {num3}, and it is of the type {type(num3)}.")
print("-" * 50)

# Step 3: Convert the string inputs to numeric values (using float to handle decimals)
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

# Print data types after conversion to show the change
print(f"After conversion, num1 is type {type(num1)}.")
print(f"After conversion, num2 is type {type(num2)}.")
print(f"After conversion, num3 is type {type(num3)}.")
print("-" * 50)

# Step 4: Perform standard arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

print(f"The sum of num1 and num2 is {addition}.")
print(f"The difference when num2 is subtracted from num1 is {subtraction}.")
print(f"The product of num1 and num2 is {multiplication}.")
print(f"The result of num1 divided by num2 is {division}.")
print("-" * 50)

# Step 5: Order of operations with and without parentheses
result1 = num1 + num2 * num3
result2 = (num1 + num2) * num3

print(f"Result without parentheses (num1 + num2 * num3): {result1}")
print(f"Result with parentheses ((num1 + num2) * num3): {result2}")
print("-" * 50)

# Step 6: Comparison operators
print(f"Is num1 greater than num2? {num1 > num2}")
print(f"Is num2 less than or equal to num3? {num2 <= num3}")
print(f"Is num3 equal to num1? {num3 == num1}")