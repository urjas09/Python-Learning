#Functions - In Python, a function is a reusable block of code that executes a specific task only when it is explicitly called. Functions help break down large programs into smaller, organized, and modular chunks, drastically eliminating code repetition.
#Two types of functions are : 
#1. Built-in Functions - These are functions that are predefined in the python interpreter. Example - print(), len(), sum(), type()
#2. User-defined Functions - A function created by the user to perform specific tasks in a program. Example - Custom business logic, calculation scripts.

#Taking an example of finding geometric mean , greater number , lesser number using functions
#Function 1
def gmean(a,b):          #called function 1
    mean = (a*b) / (a + b)
    print(mean)

#Function 2
def isGreater(a,b):     #called function 2
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")

#Function 3
def isLesser(a,b):     #called function 3
    pass    #pass is used so that the compiler understands that is part of code will be written later by the programmer and the compiler moves forward with the code without giving any error. If the function is left empty witohut using pass function that would give an error.

a = 8
b = 9
gmean(a,b)            #calling function 1
isGreater(a,b)        #calling function 2
isLesser(a,b)         #calling function 3
#NOTE - In Python, the pass statement is a null operation that does absolutely nothing when executed. It serves as a syntactic placeholder in code blocks where Python requires an indented statement, but you do not want to execute any actual logic or commands.Because Python relies on indentation to define code blocks, you cannot leave a block completely empty without triggering an IndentationError. The pass keyword solves this by satisfying Python's grammar rules while acting as a temporary "do nothing" marker.
