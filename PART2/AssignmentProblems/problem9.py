# Write a function isPrime(n) that returns True if n is prime and false otherwise
# using a loop

def is_prime(n):
    prime = True
    for i in range(2,n-1):
        if(n%i==0):
            prime = False
            break
    return prime

n = int(input("Enter the value of n here:"))
if(is_prime(n)):
    print("THE NUMBER YOU HAVE ENTERED IS A PRIME NUMBER")
else:
    print("THE NUMBER YOU HAVE ENTERED IS NOT A PRIME NUMBER")
