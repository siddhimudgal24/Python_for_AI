# Create a function to compute factorial of a number
n = int(input("Enter the value of n here:"))
def factorial(n):
    fact = 1
    i = 1
    while(i!=n+1):
        fact = fact*i
        i+=1
    return fact

print(factorial(n))