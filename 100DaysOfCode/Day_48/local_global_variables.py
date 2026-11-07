#A variable that is defined outside of a function is called a global variable and can be accessed inside a function and anywhere in the program. 
# A variable that is defined inside a function is called a local variable and can only be accessed inside that function. 

x = 4
print(x)   #prints 4

def hello():
    x = 5   #if same variable x wasnot initialized inside the function then it would have printed 4 as x is also a global variable.
    print(x) #prints 5
    print("Hello, World!")  

hello()    
#If a function defines a variable that means it is a local variable and it will not be accessible outside the function and if try to access it outside it will give an error.
#outside the function we can simply update the global variable by assigning a new value to it.
#What to do if we want to make the global value as x=5(as inside function) inside the function?
#We can use the keyword 'global' to make the global variable accessible inside the function.

y = 10
print("Global y:")
print(y)

def myfunc():   #function that is called
    global y
    y = 5
    print("Inside function y:")
    print(y)

myfunc() #function call
print("Global y after function call and value change inside function using global keyword the value changes from 10 to : ")
print(y)      
#Global keyword is used to declare that a variable is of global scope and should be accessed from the global scope.
#But it would be a good practice to avoid modifying a global variable within functions as doing so would lead to unexpected behaviour making the code difficult to debud.

