# Create a function to compute factorial of a number
def factorial(n):
    fact = 1
    i = 1
    while(i!=n+1):
        fact = fact*i
        i+=1
    return fact

n = int(input("Enter the value of n here:"))
print(factorial(20))