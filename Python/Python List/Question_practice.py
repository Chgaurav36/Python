

############################ Basic List Operations#####################
# ---
# 1.  **Create and Print:** Create a list named `fruits` with the elements "apple", "banana", "cherry", and "date". Then, print the entire list.


fruits = ["apple","banana","cherry","date"]
print(fruits)

# 2.  **Access an Element:** Access and print the second element of the `fruits` list.
print(fruits[1])

# 3.  **Modify an Element:** Change the third element of the `fruits` list to "grape" and print the updated list.
fruits[2] = "grape"
print(fruits)

# 4.  **Add an Element:** Add "mango" to the end of the `fruits` list and print the list.
fruits.append("mango")
print(fruits)

# 5.  **Remove an Element:** Remove "banana" from the `fruits` list and print the list.
fruits.remove("banana")
print(fruits)

# ############################# List Slicing and Copying########################
# ---
# 6.  **Slice a List:** Create a new list called `first_two_fruits` containing the first two elements of the `fruits` list using slicing. Print the new list.
first_two_fruits = fruits[:2]
print(first_two_fruits)

# 7.  **Slice from a Specific Index:** Create a new list called `last_two_fruits` containing the last two elements of the `fruits` list using a negative index slice. Print the new list.
last_two_fruits = fruits[-2:]
print(last_two_fruits)

# 8.  **Create a Copy:** Create a true copy of the `fruits` list called `fruits_copy` and verify that modifying an element in `fruits_copy` does not affect the original `fruits` list.

fruits_copy = fruits.copy()
fruits_copy.pop()
print(f"Fruits =  {fruits}")
print(f"Fruits copy =  {fruits_copy}")

# ############################# List Methods and Functions####################################
# ---
# 9.  **Find an Element's Index:** Find and print the index of "apple" in the `fruits` list.
fruit_name = input("Enter fruit name from above list to know the index :- ")
print(fruits)
for i in range(len(fruits)):
    if(fruits[i] == fruit_name):
        print(i)
        

# 10. **Count an Element:** Create a list `numbers = [1, 2, 3, 2, 4, 2]` and count how many times the number 2 appears.
numbers = [1, 2, 3, 2, 4, 2]
num_to_find = input("Enter number to find:- ")
counter = 0
for i in range(len(numbers)):
    if(numbers[i]) == int(num_to_find):
        counter += 1
print(f"Number {num_to_find} occured {counter} times in the list") 

# 11. **Sort a List:** Sort the `numbers` list in ascending order and the `fruits` list in descending alphabetical order. Print both sorted lists.
print(numbers.sort())
print(numbers.reverse())


# 12. **Reverse a List:** Reverse the order of the `fruits` list and print the result.

# 13. **Combine Lists:** Create another list `citrus = ["lemon", "lime"]`. Combine this list with the `fruits` list and print the combined list.

# ############################# List Comprehensions and Loops###############################
# ---
# 14. **Loop Through a List:** Use a `for` loop to iterate through the `fruits` list and print each fruit on a new line.

# 15. **Filter a List with a Loop:** Create a new empty list. Loop through a list of numbers `nums = [10, 25, 30, 45, 50, 65]` and add only the numbers greater than 40 to the new list.

# 16. **List Comprehension for a New List:** Use a list comprehension to create a new list called `squares` containing the square of each number from 1 to 10.

# 17. **List Comprehension with a Condition:** Use a list comprehension to create a new list called `even_numbers` containing only the even numbers from 1 to 20.

# ######################################Advanced Problems#############################
# ---
# 18. **Find Max and Min:** Find and print the maximum and minimum values in a list of numbers without using built-in `max()` or `min()` functions.

# 19. **Remove Duplicates:** Write code to remove duplicate elements from a list while preserving the original order. For example, `[1, 2, 2, 3, 4, 3, 5]` should become `[1, 2, 3, 4, 5]`.

# 20. **Nested Lists:** Create a nested list representing a 3x3 matrix. Access and print the element in the second row, third column.
