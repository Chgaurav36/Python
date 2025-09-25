# numbers = [4, 2, 3 ]
# print(sorted(numbers))
# numbers.reverse()
# print(numbers)



# num_to_find = input("Enter number to find:- ")
# counter = 0
# for i in range(len(numbers)):
#     if(numbers[i]) == int(num_to_find):
#         counter += 1
# print(f"Number {num_to_find} occured {counter} times in the list") 


# fruits = ["apple","banana","cherry","date"]
# fruit_name = input("Enter fruit name from above list to know the index :- ")
# print(fruits)
# for i in range(len(fruits)):
#     if(fruits[i] == fruit_name):
#         print(i)


import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_iterator = itertools.chain(list1, list2)
combined_list = list(combined_iterator)  # Convert the iterator to a list if needed
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]