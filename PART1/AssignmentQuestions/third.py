#Ask the user to enter two integers and one float
#convert them all floats and print their average
a = int(input("enter the 1st integer value here:"))
b = int(input("enter the 2nd integer value here:"))
c = float(input("enter the floating number here:"))
avg = (a+b+c)/3
# we don't have to explicitly convery a and b into floating value while calculatiing avg these value will automatically get converted into float
print("Average of three numbers is",avg)