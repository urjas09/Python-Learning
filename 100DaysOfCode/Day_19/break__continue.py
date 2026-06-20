#Break Statement - The Python break statement is used to immediately terminate a loop (either a for or while loop) when a specific condition is met.
#Example code using break
print("Mutliples of 5: ")
for i in range(1,12):                  
    print("5 *",i, "=" , 5 *(i))        #if range(12) then loop runs from 0 so in that case to get multiples of 5 from 1 to 10 perform 5 * (i+1) in the print statement

    if(i==10):
        break

#Continue Statement - The continue statement in Python skips the remaining code inside the current loop iteration and immediately forces the program to move to the next iteration. It can be used inside both for loops and while loops.
#Example code using continue
print("Natural numbers from 1 to 10: ")
for i in range(1,11):
    print(i)

    if(i==2):
      print("Skipped the second iteration.")
      continue      