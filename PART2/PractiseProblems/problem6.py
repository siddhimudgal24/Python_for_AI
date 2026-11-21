# sum of first n natural numbers (using for)
n = int(input("Enter the value of n here:"))
i = 0
sum = 0
for i in range(n+1):#n+1 because we want sum till n
    sum +=i
print(sum)