# Part 1: Positive, Negative, or Zero
number_input = input("Enter a number: ")
number = int(number_input)

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print()  # Blank line for readability

# Part 2: Age Check
age_input = input("Enter your age: ")
age = int(age_input)

if age >= 18:
    print("You are 18 or older.")
else:
    print("You are under 18.")

print()  # Blank line for readability

# Part 3: Selection (1 to 3)
choice_input = input("Enter a number from 1 to 3: ")
choice = int(choice_input)

if choice == 1:
    print("You selected Option 1: Red")
elif choice == 2:
    print("You selected Option 2: Green")
elif choice == 3:
    print("You selected Option 3: Blue")
else:
    print("Invalid selection! Please enter a number between 1 and 3.")