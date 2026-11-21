# create a function that returns largest of three
def largestofthree(a,b,c):
    if(a>b and a>c):
        return a
    elif (b>c):
        return b
    else:
        return c

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

print(largestofthree(a,b,c),"is the greatest")