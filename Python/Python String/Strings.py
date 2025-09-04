##############################      PYTHON STRINGS      #########################

a = 'Gaurav'
a = "GauravC"

#print(a)


############################   MULTILINE STRING         ####################
#Single tripple quotes
a= '''My name is gaurav chaurasia . I am 23 Years old
My name is gaurav chaurasia . I am 23 Years old
My name is gaurav chaurasia . I am 23 Years old
My name is gaurav chaurasia . I am 23 Years old
'''
#print(a)

#Double triple quotes
"""My name is gaurav chaurasia . I am 23 Years old
My name is gaurav chaurasia . I am 23 Years old
My name is gaurav chaurasia . I am 23 Years old"""



############  Strings are arrays in PYTHON    ###########


# Like any other programming language Python does not have a CHARACTER Data Type 
# Strings in Python are arrays of UNICODE characters
# We can access the characters in strings using square bracket


a = "Gaurav Chaurasia"
print(len(a))

#print(a[3])
a = ('gaurav','chaurasia','Hello')
# for x in a:
#     #print(x)
    

name = "My name is gaurav chaurasia . I am 23 Years old"

# in & not in 
print("gaurav" not in name)


# in & not in 
if "ma"  in name :   # This condition is True if any one character of the string is available.
    print("Surname is entered")
else:
    print("Surname is not entered")