# write a function that takes two integers a and b and print all even numbers between them (inclusive)
def printeven(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)
        i+=1

a = int(input("Enter the value of a here:"))
b = int(input("Enter the value of b here:"))
printeven(a,b)