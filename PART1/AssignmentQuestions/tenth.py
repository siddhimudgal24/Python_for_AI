# take a decimal value as input and print its integer part and fractional part
number = float(input("Enter the value of number here:"))
int_part = int(number)
print("the integer part is=",int_part)
fractional_part = number - int_part
print("the fractional part of the number is=>",fractional_part)
