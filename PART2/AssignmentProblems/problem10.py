# Lets create a Number guessing game
# Given a secret number (already decided by you)
# write a program for user to guess it and prints:
secret_number = int(input("Enter the number you want user to guess:"))
while(1):
    n = int(input("Guess a number"))
    if(n == secret_number):
        print("Congratulations! You guessed the correct number")
        break;
    elif(n>secret_number):
        print("Number is TOO HIGH")
    else:
        print("Number is TOO LOW")

