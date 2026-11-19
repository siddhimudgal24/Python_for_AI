# write a program to swap value of two numbers entered by the user
a = int(input("enter the 1st number"))
b = int(input("enter the 2nd number here"))
print("before swap a = ",a,"b =",b)
temp = a
a = b
b = temp
print("after swap a = ",a,"b = ",b)