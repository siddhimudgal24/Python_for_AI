#write a function to return the count the number
#of digits in a number , n
def countOfDigits(n):
    count = 0
    while(n!=0):
        rem = n%10
        count+=1
        n//=10
    return count

n = int(input("Enter the value of n here:"))
print(countOfDigits(n))
