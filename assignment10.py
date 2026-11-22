# Difference between "w" and "a" modes:
# "w" (write mode) creates a new file or completely overwrites an existing file from scratch.
# "a" (append mode) opens an existing file and adds new data to the end without deleting previous content.

# Step 2: Ask the user to enter three favorite foods, one at a time
food1 = input("Enter your first favorite food: ")
food2 = input("Enter your second favorite food: ")
food3 = input("Enter your third favorite food: ")

# Step 3: Open foods.txt in write mode ("w") and write each food on its own line
with open("foods.txt", "w") as file:
    file.write(food1 + "\n")
    file.write(food2 + "\n")
    file.write(food3 + "\n")

# Step 4: Open foods.txt in read mode ("r") and display its contents
print("\n--- Contents of foods.txt ---")
with open("foods.txt", "r") as file:
    contents = file.read()
    print(contents)

# Step 5: Open foods.txt in append mode ("a") and add one more food
food4 = input("Enter one more favorite food to append: ")
with open("foods.txt", "a") as file:
    file.write(food4 + "\n")

# Step 6: Open the file in read mode again and display each line with a line number
print("\n--- Updated Foods List ---")
with open("foods.txt", "r") as file:
    line_number = 1
    for line in file:
        print(f"{line_number}. {line.strip()}")
        line_number += 1