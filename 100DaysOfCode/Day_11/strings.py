#Strings are data types and are like an array of characters(not exactly as array of characters).
#It is a sequence or array of textual data that is enclosed with single(' ') or double(" ") quotations.

first_name = "Urja" 
last_name = 'Singh'

print("Hello, " + first_name +" " + last_name) #we can manually add spaces using empty double quotations " " 
print("Hello,", first_name,last_name) #we can also use commas- it automatically adds spaces

#If we want to have double quotations between the string we have following three ways to write it.
#1st way - using escape sequence for double quotes (\")
st1 = "Hi, I am a \"good girl\""
#2nd way - Use Single Quotes Externally(wrap the outermost layer of your string in single quotes ('...'), you can freely use double quotes inside it without escaping them) 
st2 = 'Hi, I am a \"good girl\"'
#3rd way - Triple Quotes(Triple quotes ("""...""" or '''...''') permit you to use both single and double quotes inside the string without any escape sequences.)
st3 = '''Hi, I am a \"good girl\"'''

print(st1)
print(st2)
print(st3)

#Multiline Strings - To print strings with multiple lines use triple single or double quotes.Anything within a double or single double quotation is a string and does not give error even if escape sequences are not used for new line character or for double quotes in between strings.
a = '''Hi,
I am Urja,
Nice meeting you'''

print(a)

#Accessing characters of a string
#A string is like an array of characters(not exactly as array of characters) and each part of string can be accessed by indexing and index starts from 0.
print("Accessing the string character using indexing:", first_name[0])

#Looping through a string using for loop(helps prit all the characters of string)
print("Lets print using a loop")
for character in first_name:
    print(character)