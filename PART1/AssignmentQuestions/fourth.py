#the user enters a string containing a number
# we have to convert it into 
#integer
#float
# a string again 
# print all three values with their types

a = input("enter a value here:")

integer_val = int(a)
print("the integer value of entered string",integer_val)
print("Type:",type(integer_val))

floating_val = float(a)
print("the floating value of entered string",floating_val)
print("Type:",type(floating_val))

print("the string value is",a)
print("Type:",type(a))


