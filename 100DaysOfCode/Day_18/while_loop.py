#In while loop , the cde block executes repeatedly as long as a specified condition is true. The syntax of a while loop is as follows:
#while loop - Example 1
i = 0 
while(i<3):
    print(i)
    i = i + 1
print("Done with the first loop.")

#while loop - example 2
i = int(input("Enter a number: "))
while(i<=38):
    print(i)
    i = int(input("Enter a number: "))

print("Done with the second loop.")    

#Decrementing loop
print("Decrement Loop: ")
i = 5
while(i > 0):
    print(i)
    i = i - 1    
print("Done with the loop.")    

#while loop with else
#While loops can be used for complex conditions and can also include an else block that executes when the loop condition becomes false. The else block is optional and is executed only if the loop completes without encountering a break statement.

#while loop - example 3
i = 0
while(i<3):
    print(i)
    i = i + 1
else:
    print("Loop has completed without a break statement.")

#while loop with else when break is used - Here the interpreter/program control goes out of the loop without printing the else condition.
#while loop - example 4
i = 0 
while(i<3):
    if(i==1):
        print("Breaking of loop at i = ", i)
        break
    i = i + 1
else:
    print("Loop completed.")


#NOTE - Python do not have built-in do while loops but are present in C/C++ language. 
#How to emulate do while loops in Python? Use a while true loop(infinite loop) with a conditional if along with a break at the bottom of the loop.
#True while loop - example 5

while True:
    number = int(input("Enter a positive number: "))

    if number > 0 :
        break

print(f"Congo! You entered a positive number: {number}")  # it gives the sameoutput as --> print("Congo! You entered a positive number: ", print("Congo! You entered a positive number: number"))
#NOTE(CONCEPT) - {number} is used inside an f-string (formatted string) to insert the value of a variable directly into a string.The f before the string tells Python: "Look for anything inside {} and replace it with its value."
print("Emulated do while loop completed.")
#True while loop - example 6
i = 0
while True:
    print(i)
    i = i + 1

    if(i%2==0):
      break
print("Emulated do while loop completed.") 

'''IMPORTANT NOTE-
# Python loops (while/for) do NOT create a new scope.
# Variables created inside a loop are accessible outside the loop
# as long as the loop executes at least once.

# Example:
# while True:
#     number = 10
#     break
#
# print(number)  # Output: 10

# Functions DO create a local scope.
# Variables created inside a function cannot be accessed outside it.

# Example:
# def test():
#     x = 10
#
# test()
# print(x)  # NameError

# Rule:
# if, for, while -> No new scope
# functions -> New local scope

NEW SCOPE means a visibility area (where the variable is accessible and does not give an error).
'''