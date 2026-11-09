# strings are immutable in python meand that once a string is created, it cannot be changed. Any operation for string will create a new string instead of modifying the original one.



a = "$$aman yadav &&&&&"
print(len(a))
print(a.upper())
print(a.lower())
print(a.title())
print(a.strip("$&")) # it will remove the $ and & from the string
print(a.rstrip("&"))
print(a.lstrip("$"))
print(a.replace("aman", "harry"))
print(a.split(" "))
blogheading = "introDucTion tO python"# it will convet first letter in uppearcars and rest all in lowercase 
print(blogheading.casefold()) # it will convert the string into lowercase.
print(len(blogheading))
print(blogheading.center(50))
print(len(blogheading.center(50)))
print(a.count("a")) # it will count the number of times "a" is present in the string
print(a.endswith("&&&&&")) # it will check if the string ends with "&&&&&" and return True or False
print(a.endswith("&&", 3,15)) # it will check if the string ends with "&&" from index 3 to 15 and return True 

str1 = "He's name is Dan. He is an honest man."
print(str1.find("Dan")) # it will return the index of the first occurrence of "

str1 =  "WelcomeToTheCconsole"
print(str1.isalnum()) # it will check if the string is alphanumeric or not and return True or False
str ="welcome22\n"
print(str.isalpha()) # it will check if the string is alphabetic or not and return True or False
print(str.isdigit()) # it will check if the string is digit or not and return True or False
print(str.islower()) # it will check if the string is in lowercase or not and return True or False
print(str.isupper()) # it will check if the string is in uppercase or not and return
print(str.isprintable()) # it will check if the string is printable or not and return True or False
str2 = " "
print(str2.isspace()) # it will check if the string is space or not and return True or False
print(str1.istitle()) # it will check if the string is in title case or not and return True or False means first letter of each word is capital and rest all are in lowercase
print(str1.swapcase()) # it will swap the case of the string and return the new string
