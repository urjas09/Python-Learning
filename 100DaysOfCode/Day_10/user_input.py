#In python, we take user input using the input() function.
#  The input() function takes a string as an argument by default, which is displayed to the user as a prompt. Example:name = input("Enter your name: ") Here: "Enter your name: "is the prompt that will be displayed to the user when they run the program.
#  The function then waits for the user to enter some input and press the Enter key. 
# Once the user has entered their input, it is returned as a string. 
# Since the input is returned as a string, you may need to convert it to the appropriate data type (e.g., int, float) if you want to perform calculations or other operations on it.
#1st way
a = input()
print("My name is:", a)
#2nd way
a = input("Enter your name:")
print("My name is:", a)

x = input("Enter first number:")
y = input("Enter second number:")

print(x + y) #this gives concatenated result because x and y are strings since input() returns a string by default .

print(int(x) + int(y)) #To perform addition, we need to convert them to integers.
