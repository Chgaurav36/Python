numbers = [1, 2, 3, 2, 4, 2, 2, 3, 5, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]
print(numbers.sort())
print(numbers.reverse())



num_to_find = input("Enter number to find:- ")
counter = 0
for i in range(len(numbers)):
    if(numbers[i]) == int(num_to_find):
        counter += 1
print(f"Number {num_to_find} occured {counter} times in the list") 


fruits = ["apple","banana","cherry","date"]
fruit_name = input("Enter fruit name from above list to know the index :- ")
print(fruits)
for i in range(len(fruits)):
    if(fruits[i] == fruit_name):
        print(i)