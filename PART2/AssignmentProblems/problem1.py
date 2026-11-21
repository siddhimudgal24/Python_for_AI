#Write a program that takes salary as input. Using conditional statements,
#calculate the based on these rules:
#final tax rate
#If salary < 30,000 → 5%
#If salary is 30,000–70,000 → 15%
#If salary > 70,000 → 25%

salary = float(input("Enter you salary and know your final tax rate:"))
if(salary < 30000):
    tax = 0.05*salary
    print("Your tax is",tax)
    print("Your salary after tax deduction is",salary-tax)
elif(salary < 70000):
    tax = 0.15*salary
    print("Your tax is",tax)
    print("Your salary after tax deduction is",salary-tax)
else:
    tax = 0.25*salary
    print("Your tax is",tax)
    print("Your salary after tax deduction is",salary-tax)
