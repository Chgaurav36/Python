##########################     Variables (String, Integer, Float, Boolean)      #############################

import random

print("Gaurav Chaurasia")

num = random.randint(1,10)
print(num)

name = input("Enter your fullname :- ").strip().title()
print("Your full name is :- " + name)
firstname,lastname = name.split()
print("Name after splitting " + firstname)


#################      String     ##################

first_name = "Gaurav"
print(first_name)

age = 25

print(age)
print(f"My name is {first_name}, I am {age} Years old.")




################       #Integer  and Float      #################
age = 25
quantity = 3

a = float(input("Enter number 1 :- "))
b = float(input("Enter number 2 :- "))

z = round(a + b)
print(z)





####################      Boolean  (True, False)         ######################

is_student = False

if(is_student):
    print("You are a student")
else:
    print("You are not student")