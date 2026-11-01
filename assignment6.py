# 1. Create a list named fruits containing five different fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# 2. Display the entire list
print("Initial fruit list:", fruits)

# 3. Display specific items using indexing
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])
print("Last fruit:", fruits[-1])

# 4. Ask the user for their favorite fruit and append it
favorite_fruit = input("Enter your favorite fruit: ")
fruits.append(favorite_fruit)
print("Updated list after adding favorite fruit:", fruits)

# 5. Change the second fruit in the list to "Mango"
fruits[1] = "Mango"

# 6. Remove one fruit from the list
fruits.remove("Date")

# 7. Display total number of fruits using len()
print("Total number of fruits:", len(fruits))

# 8. Use a for loop to display each fruit on a separate line
print("\nFruits in the list:")
for fruit in fruits:
    print(fruit)

# 9. Check whether "Apple" exists in the list
print()
if "Apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

# 10. Sort the list alphabetically and display it
fruits.sort()
print("Final sorted list:", fruits) 