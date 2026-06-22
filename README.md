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
| Day 13 | String Methods and String Immutability | `string_methods.py` |
| Day 14 | Conditional Statements (if, elif, else, Nested If) | `if_else_conditional_statements.py` |
| Day 15 | Exercise 2 - Greeting Program Based on Time | `exercise_02.py` |
| Day 16 | Match Case Statements | `match_case_statements.py` |
| Day 17 | For Loops and range() | `for_loop.py` |
| Day 18 | While Loops | `while_loop.py` |
| Day 19 | Break and Continue Statements | `break_continue.py` |
| Day 20 | Functions in Python | `functions.py` |
| Day 21 | Function Arguments and Return Statements | `FunctionArguments.py` |
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

# Day 14 - Conditional Statements in Python

## Concepts Learned

### Conditional Statements
Conditional statements allow a program to make decisions based on conditions.

### Comparison Operators

The following comparison operators return either `True` or `False`:

- `<` → Less than
- `>` → Greater than
- `<=` → Less than or equal to
- `>=` → Greater than or equal to
- `==` → Equal to
- `!=` → Not equal to

---

## Topics Covered

### 1. User Input with Conditional Checks

- Taking input using the `input()` function.
- Converting input to integer using `int()`.
- Using comparison operators to evaluate conditions.

Example:

```python
age = int(input("Enter your age: "))

print(age < 18)
print(age > 18)
print(age <= 18)
print(age >= 18)
print(age == 18)
print(age != 18)
```

---

### 2. if-else Statements

Used to execute different blocks of code depending on whether a condition is `True` or `False`.

Example:

```python
if age > 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

---

### 3. Indentation in Python

- Indentation defines the scope of a block of code.
- Python uses indentation instead of braces `{}`.
- Consistent indentation is mandatory.

Example:

```python
if age > 18:
    print("You are eligible to vote.")

print("This line is outside the if block.")
```

---

### 4. elif Statements

- `elif` stands for "else if".
- Used to test multiple conditions sequentially.
- The first matching condition gets executed.

Example:

```python
num1 = int(input("Enter a number: "))

if num1 < 0:
    print("The number is negative.")
elif num1 == 0:
    print("The number is zero.")
elif num1 == 999:
    print("The number is special.")
else:
    print("The number is positive.")
```

---

### 5. Nested if Statements

- An `if` statement inside another `if` or `elif` block.
- Useful when additional checking is required after a condition becomes true.

Example:

```python
num2 = int(input("Enter another number: "))

if num2 < 0:
    print("The number is negative.")

elif num2 > 0:

    if num2 <= 10:
        print("The number is between 1-10.")

    elif num2 > 10 and num2 <= 20:
        print("The number is between 11-20.")

    else:
        print("The number is greater than 20.")

else:
    print("The number is zero.")
```

---

## File

- `if-else_conditional_statements.py`

---

## Key Takeaways

- Conditional statements help programs make decisions.
- Comparison operators return boolean values (`True` or `False`).
- `if` executes code when a condition is true.
- `else` executes code when all previous conditions are false.
- `elif` allows testing multiple conditions.
- Nested `if` statements enable more detailed decision-making.
- Proper indentation is essential in Python and determines code blocks.

---

## Sample Learning Outcomes

After completing Day 14, I can:

- Take user input and evaluate conditions.
- Use comparison operators effectively.
- Write `if-else` statements.
- Use multiple conditions with `elif`.
- Create nested conditional structures.
- Understand the importance of indentation in Python.

---

Day 14 of #100DaysOfCode 🚀

# Day 15 - Greeting Program

## Concepts Learned

- User input using `input()`
- Type conversion using `int()`
- Comparison operators
- `if`, `elif`, and `else` statements
- Input validation
- Code optimization

---

## Exercise

Created a program that greets the user based on the entered hour.

- 0–11 → Good Morning Sir!
- 12–17 → Good Afternoon Sir!
- 18–23 → Good Evening Sir!
- Invalid hour → Error message

---

## File

- `exercise_02.py`

---

## Key Takeaways

- Applied conditional statements to a real-world scenario.
- Learned input validation.
- Practiced writing cleaner and optimized conditions.
- Understood that the same problem can have multiple solutions.

---

Day 15 of #100DaysOfCode 🚀

# Day 16 - Match Case Statements in Python

## Concepts Learned

- Introduction to `match-case` statements (Python 3.10+)
- Alternative to `switch-case` found in other programming languages
- Pattern matching using different cases
- Default case using `case _`
- Using conditions inside `match-case`

---

## Topics Covered

### Basic Match Case

- Matching a value against multiple cases.
- Executing the matching block of code.

### Default Case

- Using `case _` when no case matches.

### Conditional Match Case

- Using conditions with match-case for more flexible decision-making.

---

## File

- `match_case_statements.py`

---

## Key Takeaways

- `match-case` improves code readability when checking multiple values.
- Python does not require `break` statements in match-case blocks.
- `case _` acts like the default case.
- Conditions can also be used within match-case statements.

---

Day 16 of #100DaysOfCode 🚀

# Day 17 - For Loops in Python

## Concepts Learned

- Introduction to `for` loops
- Iterating over strings
- Iterating over lists
- Nested loops
- Using the `range()` function
- Understanding `start`, `stop`, and `step` parameters

---

## Topics Covered

### Iterating Over a String

- Accessing each character one by one using a `for` loop.

### Iterating Over a List

- Accessing each element of a list.
- Using nested loops to iterate through characters of each string in the list.

### The `range()` Function

- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

### Step Parameter

- Controls the increment between generated numbers.
- Example: `range(1, 10, 2)` generates odd numbers from 1 to 9.

---

## File

- `for_loop.py`

---

## Key Takeaways

- `for` loops are used to iterate over sequences.
- Strings and lists are iterable objects.
- Nested loops allow iteration within iteration.
- `range()` helps generate sequences of numbers efficiently.
- The `step` parameter controls how values increase or decrease during iteration.

---

Day 17 of #100DaysOfCode 🚀

# Day 18 - While Loops in Python

## Concepts Learned

- Introduction to `while` loops
- Incrementing and decrementing loops
- Taking user input inside a loop
- `while-else` statements
- Using `break` with loops
- Infinite loops using `while True`
- Emulating a do-while loop in Python
- Scope behavior in loops

---

## Topics Covered

### Basic While Loop

- Repeating code while a condition remains true.
- Incrementing a counter variable.

### User-Controlled While Loop

- Taking input repeatedly until a condition becomes false.

### Decrementing Loop

- Counting backwards using a while loop.

### While-Else Statement

- `else` executes when the loop finishes normally.
- `else` does not execute if the loop is terminated using `break`.

### Break Statement

- Used to exit a loop immediately.

### Infinite Loop

- Using `while True` to create a loop that runs indefinitely.
- Stopping the loop using `break`.

### Emulating Do-While Loop

- Python does not have a built-in `do-while` loop.
- Similar behavior can be achieved using `while True` and `break`.

### Scope in Loops

- `if`, `for`, and `while` blocks do not create a new scope.
- Variables created inside loops can be accessed outside the loop.
- Functions create a local scope.

---

## File

- `while_loop.py`

---

## Key Takeaways

- `while` loops execute as long as a condition is true.
- `break` can terminate a loop immediately.
- `while-else` behaves differently when `break` is used.
- `while True` is useful for input validation and menu-driven programs.
- Python does not support a native `do-while` loop.
- Loops do not create a new scope, but functions do.

---

Day 18 of #100DaysOfCode 🚀

# Day 19 - Break and Continue Statements in Python

## Concepts Learned

- break statement
- continue statement
- Using break in loops
- Using continue in loops
- Controlling loop execution flow

---

## Topics Covered

### Break Statement

- Used to immediately terminate a loop.
- Program control exits the loop as soon as `break` is encountered.
- Can be used with both `for` and `while` loops.

### Continue Statement

- Skips the remaining code in the current iteration.
- Moves directly to the next iteration of the loop.
- Useful when certain values need to be ignored.

### Practical Examples

- Printing multiples of 5 using a loop and stopping execution with `break`.
- Skipping a specific iteration using `continue`.
- Understanding the difference between terminating a loop and skipping an iteration.

---

## File

- `break_continue.py`

---

## Key Takeaways

- `break` completely exits a loop.
- `continue` skips only the current iteration.
- Both statements help control loop behavior efficiently.
- They make programs cleaner and reduce unnecessary conditions.

---

Day 19 of #100DaysOfCode 🚀

# Day 20 - Functions in Python

## Concepts Learned

- Built-in functions
- User-defined functions
- Function definition using `def`
- Parameters and arguments
- Function calls
- `pass` statement

---

## Topics Covered

### Functions
- Reusable blocks of code used to perform specific tasks.

### User-defined Functions
- Created using the `def` keyword.
- Can accept parameters and be called multiple times.

### Pass Statement
- Placeholder used when a function has no implementation yet.

---

## File

- `functions.py`

---

## Key Takeaways

- Functions improve code reusability and readability.
- Parameters make functions flexible.
- `pass` allows creating empty functions without errors.

---

Day 20 of #100DaysOfCode 🚀

# Day 21 - Function Arguments in Python

## Concepts Learned

- Default Arguments
- Keyword Arguments
- Required Arguments
- Return Statement
- Variable Length Arguments (`*args`)
- Keyword Variable Length Arguments (`**kwargs`)

---

## Topics Covered

### Function Arguments
- Different ways to pass values to functions.

### Return Statement
- Used to send a value back to the calling function.

### Variable Length Arguments
- `*args` allows multiple positional arguments.
- `**kwargs` allows multiple keyword arguments.

---

## File

- `FunctionArguments.py`

---

## Key Takeaways

- Functions can accept arguments in different ways.
- `return` makes functions reusable and powerful.
- `*args` and `**kwargs` provide flexibility when the number of arguments is unknown.

---

Day 21 of #100DaysOfCode 🚀