hour1 = int(input("Enter the hour (0-23): "))

if hour1 < 0 or hour1 > 23:
    print("Invalid Hour! Please enter a valid hour (0-23).")
elif hour1 >=0 and hour1 <12:
    print("Good Morning Sir!")
elif hour1 >=12 and hour1<18:
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")    

#Simple optimization since the invalid hour condition is already checked, we can directly check for the valid conditions without checking for the range again.
hour2 = int(input("Enter the hour (0-23): "))
if hour2 < 0 or hour2 > 23:
    print("Invalid Hour! Please enter a valid hour (0-23).")
elif hour2<12:
    print("Good Morning Sir!")
elif hour2<18:
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")
