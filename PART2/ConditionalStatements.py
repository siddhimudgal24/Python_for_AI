#Example - 1
age = int(input("Enter age:"))

if age>=18:
    print("You can Vote")
    print("You can Drive")
else:
    print("You can't Vote")
    print("You can't Drive")

#Example - 2 =  Traffic Lights

color = input("Enter Color:")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else: 
    print("Wrong Color")

#Example - 3 = Logical Operators in Expressions
age2 = int(input("Enter age2:"))

if age2<13:
    print("Child")
elif (age2>=13 and age2<18):
    print("teenager")
else:
    print("adult")