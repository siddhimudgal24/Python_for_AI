# write a function that prints the digits of a number n
# eg. n = 312, there are 3 digits 3,1 and 2 and we need to print them
def digitsinNum(n):
    while(n!=0):
        rem = n%10
        print(rem)
        n//=10

# in python we use / => for normal division , it always returns a floating point number
# in python we use // => for floor division , it removes the decimal part by rounding down to the nearest integer

n = int(input("Enter the value of n here:"))
digitsinNum(n)   

# this approach prints the individual integer values of the given or entered number 
# but in reverse order to print in the same order we have to use recursion separately or by using list like storing values in a list and then printing them in the same order


