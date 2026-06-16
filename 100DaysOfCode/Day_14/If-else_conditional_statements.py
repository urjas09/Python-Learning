#Conditional Statements: These statements are used to perform different actions based on different conditions.
#In Python, we use `if`, `elif`, and `else` statements to perform conditional operations. The `if` statement is used to test a specific condition, the `elif` statement is used to test multiple conditions, and the `else` statement is used to execute a block of code if none of the conditions are true.
#Conditional Operators: These operators are used to compare values and return a boolean result (True or False). The most commonly used conditional operators in Python are: <, >, <=, >=, ==, !=. 

#Taking user input
a = int(input("Enter your age: "))
#Conditional operators
print(a<18) #It will return True if the age is less than 18, otherwise it will return False.
print(a>18) #It will return True if the age is greater than 18,otherwise it will return False.
print(a<=18) #It will return True if the age is less than or equal to 18, otherwise it will return False.
print(a>=18) #It will return True if the age is greater than or equal to 18, otherwise it will return False.
print(a==18) #It will return True if the age is equal to 18, otherwise it will return False.
print(a!=18) #It will return True if the age is not equal to 18, otherwise it will return False.

#if-else statements
if a>18:
    print("You are  eligible to vote.")
else:
    print("You are not eligible to vote.")

#Indentaion in Python
#In Python, indentation is used to define the scope of a block of code. It is important to maintain consistent indentation throughout the code.
#for eg:
if a>18:
    print("You are eligible to vote.")
print("This line is outside the if block.") #This line is outside the if block (no indentation) and will be executed regardless of the condition. So, it will be executed even if the condition is false.

#elif statements - It is used to test multiple conditions. It is short for "else if". It allows you to check multiple conditions and execute different blocks of code based on the condition that is true.

num1 = int(input("Enter a number: "))
if num1<0:
    print("The number is negative.")
elif num1==0:
    print("The number is zero.")
elif num1==999:
    print("The number is special.")    
else:
    print("The number is positive.")

#Nested if statements - It is used to test multiple conditions within another if statement. It allows you to check for additional conditions if the first condition is true. We can use if, elif, and else statements within another if statement as well.
num2 = int(input("Enter another number: "))
if(num2<0):
    print("The number is negative.")
elif(num2>0):
    if(num2<=10):
        print("The number is between 1-10.")
    elif(num2>10 and num2<=20):
        print("The number is between 11-20.")   
    else:
        print("The number is greater than 20.") #this is the elif for second if statement. It will be executed if the first condition (num2<=10) is false and the second condition (num2>10 and num2<=20) is also false, which means num2 is greater than 20.
else:
        print("The number is zero.") #this is the else for first if statement. It will be executed if the first condition (num2<0) is false and the second condition (num2>0) is also false, which means num2 is equal to 0.

