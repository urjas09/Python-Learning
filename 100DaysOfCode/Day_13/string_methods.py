#String Methods
#Strings are immutable in Python, which means that once a string is created, it cannot be modified. However, Python provides a variety of built-in string methods that allow you to perform operations on strings and create new strings based on the original.
#Here are some commonly used string methods in Python:
#1. `upper()`: Converts all characters in the string to uppercase.
a = "Urja"
print(a.upper()) #we cannot change the original string but we can create a copy of the string with the modified value and whenever we use the methods it gives us a new string where all the letters will be in uppercase.
#2. `lower()`: Converts all characters in the string to lowercase.
b = "URJA"
print(b.lower()) #we cannot change the original string but we can create a copy of the string with the modified value and whenever we use the methods it gives us a new string where all the letters will be in lowercase.
#Basically strings work on our existing string and gives us a new string with the modified value.
#3. `rstrip()`: Removes any trailing characters (characters at the end of a string), based on the argument passed. If no argument is passed, it removes trailing whitespace.
c= "Urja!!!!"
print(c.rstrip("!")) #we cannot change the original string but we can create a copy of the string with the modified value and whenever we use the methods it gives us a new string where all the trailing exclamation marks will be removed.
#4. `replace()`: Replaces a specified phrase with another specified phrase. It returns a new string with the replacements.
print(a.replace("Urja", "Kajal")) #we cannot change the original string but we can create a copy of the string with the modified value and whenever we use the methods it gives us a new string where all the occurrences of "Urja" will be replaced with "Kajal".
print(a) #the original string remains unchanged.
#5 `split()`: Splits a string into a list where each word is a list item. The split is done at the specified separator (default is any whitespace).
d= "Urja Singh"
print(d.split(" "))
#6. `capitalize()`: Converts the first character of the string to uppercase and the rest to lowercase.There is no effect if the first letter is already capital or the other letters except first are already small.
blog_title = "python programming"
print(blog_title.capitalize()) 
