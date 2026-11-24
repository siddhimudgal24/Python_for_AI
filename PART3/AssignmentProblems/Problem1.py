# Ask the user for a string and check whether it is 
# a palindrome or not


#reversing a string using slicing in strings
string = input("Enter the string that you want to check:")
s = string[::-1]

if(s==string):
    print("The string you have entered is a palindrome")
else:
    print("The string you have entered is a not a palindrome")

