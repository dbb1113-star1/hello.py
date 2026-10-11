# ==========================================
# Part 1: Positive, Negative, or Zero
# ==========================================
user_number_input = input("Enter a number: ")
number = int(user_number_input)

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print()  # Empty line for clean formatting

# ==========================================
# Part 2: Age Check
# ==========================================
user_age_input = input("Enter your age: ")
age = int(user_age_input)

if age >= 18:
    print("You are 18 or older.")
else:
    print("You are under 18.")

print()  # Empty line for clean formatting

# ==========================================
# Part 3: Number Choice (1 to 3)
# ==========================================
choice = input("Enter a number from 1 to 3: ")

if choice == "1":
    print("You selected option 1: Welcome to the Python program!")
elif choice == "2":
    print("You selected option 2: Keep up the great coding work!")
elif choice == "3":
    print("You selected option 3: Python conditional logic is fun!")
else:
    print("Invalid selection! Please enter a number between 1 and 3.")