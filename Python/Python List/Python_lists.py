##################################      PYTHON LISTS        #####################

# Python lists are used to store multiple data/items in a single variable
# Lists are one of pythons 4 inbuilt data types.Other three are Tuple,Set,Dictonary all with different qualities and usage.


# Lists are created usnig square bracket
my_lists  = ["Gaurav", "Sakshi", "Omprakash", "Pankaj"]
print(my_lists)

#Lists are ORDERED , CHANGEABLE , and ALLOWS DUPLICATE VALUES
###############################################################################################################
# Method     ################Description######################
# append()	--> Adds an element at the end of the list
# clear()	--> Removes all the elements from the list
# copy()	--> Returns a copy of the list
# count()	--> Returns the number of elements with the specified value
# extend()	--> Add the elements of a list (or any iterable), to the end of the current list
# index()	--> Returns the index of the first element with the specified value
# insert()	--> Adds an element at the specified position
# pop()	    --> Removes the element at the specified position
# remove()	--> Removes the item with the specified value
# reverse()	--> Reverses the order of the list
# sort()	--> Sorts the list

# x = print(my_lists[3])
# print(type(x))    #output --->  <class 'NoneType'>

# print(my_lists[2:])

for x in my_lists:
    print(x)



    
    