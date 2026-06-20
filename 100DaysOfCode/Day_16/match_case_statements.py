#Match Case Statements - Match case statements are a new feature introduced in Python 3.10. They allow for more readable and concise code when dealing with multiple conditions.
#Match case statements are similar to switch case statements in other programming languages. They allow you to match a value against multiple cases and execute the corresponding block of code.
#Unlike c/c++/java, python does not have a switch case statement. Instead, we can use match case statements to achieve similar functionality.
#In puthon we do not use break satements in match case statements. In languages such as c/c++/java, we use break statements to exit the switch case statement after executing a case. In python, we do not need to use break statements in match case statements. Once a case is matched, the corresponding block of code is executed and the match case statement is exited automatically.

x = int(input("Enter a number:"))

match x:
    case 1:
        print("Number is 1")
    case 2:
        print("Number is 2")
    case 3:
        print("Number is 3")
    case _:
        print("Number is not 1, 2, or 3")


#We can also use if statements inside match case statements to check for multiple conditions. This allows us to have more complex logic inside our match case statements.

y = int(input("Enter a number:"))

match y:
    case 1:
        print("Number is 1")
    case 2:
        print("Number is 2")
    case _ if y == 3:
        print("Number is 3")
    case _:
        print("Number is not 1, 2, or 3")
