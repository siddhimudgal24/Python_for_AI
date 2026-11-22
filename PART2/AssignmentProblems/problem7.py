# Design a program to continuously input a number 
# n from user and print if it is positive 
# or negative until the user enters quit
while(1):
    n = input("Enter the value of n here: and if you want to quit ,Type QUIT")
    if(n == "Quit"):
        break
    if(int(n)<0):
        print("The Number you have entered is a negative number")
    else:
        print("The Number you have entered is a Positive number")

