#ask for p,r,t and convert them into float and 
#calculate si
principal = float(input("Enter the value of principal here:"))
rate = float(input("Enter the rate here:"))
time = float(input("Enter the time here:"))

simple_interest = (principal*rate*time)/100
print(simple_interest)

