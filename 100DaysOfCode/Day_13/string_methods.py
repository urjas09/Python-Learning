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
#7. center(width, fillchar): Returns a centered string of a specified width. The fillchar is the character used to fill the remaining space on either side of the string. The default fillchar is a space.
str1 = "Welcome to the Console!!!"
print(str1.center(50))#left spaces + original string + right spaces 
print(str1.center(50, "*")) #we cannot change the original string but we can create a copy of the string with the modified value and whenever we use the methods it gives us a new string where the original string is centered within a field of a specified width, and the remaining space is filled with a specified character (in this case, "*").
print(len(str1.center(50)))
print(len(str1))
#8. count() : Returns the number of occurrences of a specified substring in the string.
print(str1.count("!!!"))
#9. endswith() : Returns True if the string ends with the specified suffix, otherwise returns False.
print(str1.endswith("!!!"))
#10. startswith() : Returns True if the string starts with the specified prefix, otherwise returns False.
print(str1.startswith("Welcome"))
print(str1.endswith("to",4,10))
#11. find() : It searches for the first occurrenceof the value and returns the index of the value if it is found in the string. If it is not found, it returns -1.
print(str1.find("to"))
#12. index() : It searches for the first occurrence of the value and returns the index of the value if it is found in the string. If it is not found, it raises a ValueError.
print(str1.index("to"))
#13. isalnum() : Returns True if all characters in the string are alphanumeric (letters and numbers(A-Z, a-z, 0-9)), otherwise returns False.
print(str1.isalnum())
#14. isalpha() : Returns True if all characters in the string are alphabetic (letters only (A-Z, a-z)), otherwise returns False.
print(str1.isalpha()) #It returns False because there are spaces and exclamation marks in the string.
#15. islower() : Returns True if all characters in the string are lowercase, otherwise returns False.
st = "hello world"
print(st.islower()) #It returns True because all the characters in the string are lowercase.
#16. isupper() : Returns True if all characters in the string are uppercase, otherwise returns False.
st1 = "HELLO WORLD"
print(st1.isupper()) 
#17. isprintable() : Returns True if all characters in the string are printable (i.e., they can be printed on the screen), otherwise returns False.
st2 = "Hello\nWorld"
print(st2.isprintable()) #it returns false because the string contains a newline character (\n) which is not printable. If we remove the newline character, it will return True.
#18. isspace() : Returns True if all characters in the string are whitespace, otherwise returns False.
st2 = "   "
print(st2.isspace()) 
#19. istitle() : Returns True if the string is a titlecased string (i.e., each word starts with an uppercase letter followed by lowercase letters), otherwise returns False.
st3 = "Hello World"
print(st3.istitle())
#20. swapcase() : Returns a new string where all uppercase letters are converted to lowercase and all lowercase letters are converted to uppercase.
st4 = "Hello World"
print(st4.swapcase())
#21. title() : Returns a new string where the first character of each word is converted to uppercase and the rest are converted to lowercase.
st5 = "hello world"
print(st5.title())

#Note:We can overwrite the original string by assigning the modified string back to the original variable. For example: 
s = "Urja"
s="Urja Singh" #Now the original string is overwritten with the new value.
print(s)