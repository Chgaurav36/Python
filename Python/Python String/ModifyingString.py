# PYTHON has a built-in methods to use on strings
# Upper Case                            ----Converts to upper case
# Lower Case                            ----Converts to lower case
# Remove white space                    ----Remove space from starting and endng of the string  
# Replace String                        ----Replaces a character or string
# Split Stiring                         ----Splits strings
# Capitalize String                     ----First letter of strings are converted to uppercase

#################   UPPER   ###############
name = "gaurav chaurasia"
print(name.upper())


#################   Lower   ###############
name = "GaurAv ChaUrasia"
print(name.lower())


#################   Whitespace(Strip) ###############
name = "      gaurav chaurasia     "
print(name.strip())


#################   Replace String   ###############
name = "cat"
print(name.replace("c","m"))



#################   Split String   ###############
#Split method returns a list 

animals = "dog,cat,horse,lion"
print(animals.split(","))     #Output = ['dog', 'cat', 'horse', 'lion']




#################   Capatilize String   ###############
name = "gaurav"
print(name.capitalize())