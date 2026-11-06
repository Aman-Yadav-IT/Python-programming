""" typecasting in python is used to convert one data type into another data type for example
 we can convert an integer into a string 
 or a string into an integer using type casting in python"""

a = "5"
b = "10"
c = int(a) + int(b) # here we are converting the string into integer using int() function
print(c) # output will be 15
# we can also convert an integer into a string using str() function
a = 5
b = 12
c = str(a) + str(b) # here we are converting the integer into string using str() function
print(c) # output will be 512
# we can also convert a float into an integer using int() function
a = 5.5
b = 10.5
c = int(a) + int(b) # here we are converting the float into integer using int() function
print(c) # output will be 15 

# we can also convert an integer into a float using float() function
a = 5   
b = 12
c = float(a) + float(b) # here we are converting the integer into float using float() function
print(c) # output will be 17.0
