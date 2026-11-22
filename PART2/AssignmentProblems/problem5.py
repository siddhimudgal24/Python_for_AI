#Write a function to return the sum of digits of a
#number , n

def sumOfDigits(n):
    sum = 0
    while(n!=0):
        rem = n%10
        sum+=rem
        n//=10
    return sum

n = int(input("Enter the value of n here:"))
print(sumOfDigits(n))
