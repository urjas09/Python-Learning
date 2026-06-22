''' Function Arguments-
There are 4 types of arguments to provide in a function:
1. Default Arguments
2. Keyword Arguments
3. Required Arguments
4. Variable Length Arguments
'''
#1. Default Arguments - We can provide a default value while crating a function. In this way even if a value is not provided by the function call, the function assumes the default value.
def average(a=9 , b=1):  #default values are a = 9 and b = 1. Also , if avalue is provided and also it's default value is provided so the value provided by the funxtion call is considered.
    print("Average is: ", (a+b)/2)

average(a=10)
#2. Keyword Argument - We can provide arguments as key=value so then the interpreter recognizes the value by the parameter name. Hence the order in which the arguments are passed do not matter.
average(b=21 , a = 9)

#3. Required Arguments - In case we do not pass the value as key=value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed must match the actual funnction definition.

#Example 1 - when number of arguments do not match the actual function definition
'''
def name(fname,mname,lname):
    print("Hello", fname,mname,lname)

name('Peter', 'Quill')       #gives error - TypeError: name() missing 1 required positional argument: 'lname'
'''
#Example 2 - when number of arguments match the actual function definition
def name(fname,mname,lname):
    print("Hello!", fname,mname,lname)

name('Peter', 'Ego', 'Quill') #executes successfully

#RETURN STATEMENT - It is used to return the value of the expression back to the calling function.
def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
        i=i+1
    #return 7  #when mutliple return statements are present the very first statement is executed by the interpreter and the the return statements below that are ignored.    
    return sum/len(numbers)  
      
c = average(4,5,6,1)
print("Average of 4 numbers:", c)


#Study the below section when you have studied about tupleand dictionary.

#4. Variable Length Arguments - Sometimes we need to pass more arguments than those defined in the actual function. This can be done using variable length arguments.

#There are 2 ways:
#1. Arbitrary Arguments(*args) - When you create a function , pass a * before the parameter name  while defining the function. The function processes the arguments in the form of a tuple.
#  This is variable-length positional arguments (*args). It allows you to pass multiple values: name1('Peter', 'Ego', 'Quill')
def name1(*name):
    print("Hello!", name[0],name[1],name[2])

name1('Peter', 'Ego', 'Quill')

#2. Keyword Arbitrary Arguments(**kwargs) - When you create a function , pass a ** before the parameter name  while defining the function. The function processes the arguments in the form of a dictionary.
#This is variable-length keyword arguments (**kwargs). It allows you to pass multiple key-value pairs: name2(mname='Ego', fname='Peter', lname='Quill')
def name2(**name):
    print("Hello!", name['fname'],name['mname'],name['lname'])

name2( mname = 'Ego',fname = 'Peter', lname = 'Quill')

#NOTE - *args and **kwargs provide flexibility when the number of arguments is unknown.