#Lets create a simple calculator that performs arithmetic operations.
#Create a function that performs addition,subtraction, multiplication
# or division based on the operation parameter
# operation parameter can have values '+','-','*','/'


# we are solving this question with if,elif and else statement 
# we can also use match case to solve this 
def calculator(a,b,operation):
    if(operation=='+'):
        print("The operator you have entered is a Addition operator")
        print("Addition is",a+b)
    elif(operation == '-'):
        print("The operator you have entered is a Subtraction operator")
        print("Subtraction is",a-b)
    elif(operation == '*'):
        print("The operator you have entered is a Multiplication operator")
        print("Multiplication is",a*b)
    else:
        print("The operator you have entered is a division operator")
        print("Division is",a/b)

a = int(input("Enter the value of a here:"))
b = int(input("Enter the value of b here:"))
operator = input("Enter the operator for the operation you want to perform:")
calculator(a,b,operator)