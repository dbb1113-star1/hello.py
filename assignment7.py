# ==========================================
# Part 1: Working with Tuples
# ==========================================

# 1. Create a tuple named days containing the seven days of the week.
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# 2. Display the entire tuple using print().
print("Entire tuple of days:")
print(days)
print()

# 3. Display specific elements using indexing:
print(f"First day: {days[0]}")
print(f"Fourth day: {days[3]}")
print(f"Last day: {days[-1]}")
print()

# 4. Display the total number of elements in the tuple using len().
print(f"Total number of days: {len(days)}")
print()

# 5. Use a for loop to display each day on a separate line.
print("Days of the week:")
for day in days:
    print(day)
print()

# 6. Check whether "Monday" exists in the tuple using if/else.
if "Monday" in days:
    print("Monday is in the tuple.")
else:
    print("Monday is not in the tuple.")
print()

# 7 & 8. Attempt to change the first element and explain why it fails.
# days[0] = "Holiday"  
# EXPLANATION: Tuples in Python are immutable data structures, meaning their elements 
# cannot be changed, added, or removed after creation. Attempting to assign a new 
# value to an index raises a TypeError. The line above has been commented out so 
# the program runs successfully.


# ==========================================
# Part 2: Working with Sets
# ==========================================

# 1. Create a set named colors containing four values.
colors = {"Red", "Blue", "Green", "Yellow"}

# 2. Display the entire set using print().
print("Initial set of colors:")
print(colors)
print()

# 3. Use add() to add "Purple" to the set.
colors.add("Purple")

# 4. Use remove() to remove "Yellow" from the set.
colors.remove("Yellow")

# 5, 6, & 7. Prompt user for favorite color and add it to the set.
favorite_color = input("Enter your favorite color: ")
colors.add(favorite_color)
print()

# 8. Use a for loop to display each color in the set on a separate line.
print("Current colors in the set:")
for color in colors:
    print(color)
print()

# 9. Display total number of unique colors using len().
print(f"Total number of unique colors: {len(colors)}")
print()

# 10 & 11. Create set1 and set2 with specified values.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 12 & 13. Perform and display set operations.
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union (all unique elements): {set1.union(set2)}")
print(f"Intersection (common elements): {set1.intersection(set2)}")
print(f"Difference (elements in set1 not in set2): {set1.difference(set2)}")