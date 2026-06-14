# Python Learning Repository

This repository contains my Python learning journey and solutions completed as part of my **100 Days of Code** challenge.

---

## Progress

| Day | Topic | File |
|-----|--------|------|
| Day 01 | Hello World | `hello_world.py` |
| Day 10 | User Input in Python | `user_input.py` |
| Day 11 | Strings in Python | `strings.py` |
| Day 12 | String Slicing | `string_slicing.py` |

---

## Day 10 - User Input in Python

### Concepts Covered
- Taking user input using `input()` function
- Using prompts with `input()`
- Storing user input in variables
- Understanding that `input()` returns a string by default
- String concatenation
- Type conversion using `int()`
- Integer addition

### Sample Output

```text
Enter your name: Urja
My name is: Urja

Enter first number: 10
Enter second number: 20

1020 
30
```

Day 10 of #100DaysOfCode 🚀

# Day 11 - Strings in Python

## Concepts Learned
- Introduction to Strings
- String Concatenation using `+`
- Using commas in `print()`
- Including quotes inside strings
- Multiline Strings
- String Indexing
- Looping through Strings using `for` loop

## Output
```text
Hello, Urja Singh
Hello, Urja Singh

Hi, I am a "good girl"
Hi, I am a "good girl"
Hi, I am a "good girl"

Hi,
I am Urja,
Nice meeting you

Accessing the string character using indexing: U

Lets print using a loop
U
r
j
a
```

## Key Takeaway
Strings are sequences of characters that can be accessed using indexing and traversed using loops.

---
Day 11 of #100DaysOfCode 🚀

# Day 12 - String Slicing in Python

## Concepts Learned
- Finding the length of a string using `len()`
- String Slicing using `[start:end]`
- Negative Slicing
- Understanding why some slices return an empty string

## Output
```text
Length of the string is: 5

Substring from index 0 to 4: Mang
Substring from index 1 to 4: ang
Substring from index 0 to 5 (omitting start_index): Mango

Substring from index 0 to -3: Ma
Substring upto index -3 (omitting start_index): Ma
Substring from index -1 to index -3 to end:
Substring from index -3 to -1: ng
```

## File
- `string_slicing.py`

## Key Takeaway
String slicing allows us to extract specific parts of a string using positive and negative indices. The start index is inclusive, while the end index is exclusive.

---
Day 12 of #100DaysOfCode 🚀

# Day 13 - String Methods in Python

## Concepts Learned

### String Immutability
- Strings are immutable in Python.
- String methods do not modify the original string.
- They return a new string with the desired changes.

### String Methods Covered

- `upper()` → Converts all characters to uppercase.
- `lower()` → Converts all characters to lowercase.
- `rstrip()` → Removes trailing characters from the right side of a string.
- `replace()` → Replaces a specified substring with another substring.
- `split()` → Splits a string into a list based on a separator.
- `capitalize()` → Converts the first character to uppercase and the rest to lowercase.
- `center(width)` → Centers a string within a specified width using spaces.
- `center(width, fillchar)` → Centers a string using a custom fill character.
- `count()` → Counts the occurrences of a specified substring.
- `endswith()` → Checks whether a string ends with a specified suffix.
- `startswith()` → Checks whether a string starts with a specified prefix.
- `find()` → Returns the index of the first occurrence of a substring.
- `index()` → Returns the index of a substring and raises an error if not found.
- `isalnum()` → Checks if all characters are alphanumeric.
- `isalpha()` → Checks if all characters are alphabetic.
- `islower()` → Checks if all alphabetic characters are lowercase.
- `isupper()` → Checks if all alphabetic characters are uppercase.
- `isprintable()` → Checks whether all characters are printable.
- `isspace()` → Checks whether a string contains only whitespace characters.
- `istitle()` → Checks whether each word starts with an uppercase letter.
- `swapcase()` → Converts uppercase letters to lowercase and vice versa.
- `title()` → Converts the first character of every word to uppercase.

---

## Sample Output

```text
URJA
urja
Urja
Kajal
Urja

['Urja', 'Singh']

Python programming

            Welcome to the Console!!!
************Welcome to the Console!!!************
50
25

3
True
True
7
7
False
False
True
True
False
True
True
hELLO wORLD
Hello World

Urja Singh
```

---

## File

- `string_methods.py`

---

## Key Takeaways

- Strings in Python are immutable.
- Most string methods return a new string instead of modifying the original one.
- String methods make text manipulation easier and more efficient.
- Validation methods such as `isalnum()`, `isalpha()`, `islower()`, and `isupper()` help verify string contents.
- Formatting methods such as `capitalize()`, `title()`, `swapcase()`, and `center()` improve text presentation.

---

Day 13 of #100DaysOfCode 🚀