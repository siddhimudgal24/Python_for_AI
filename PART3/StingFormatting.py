# string formatting is the process of creating 
# dynamic strings by inserting values from 
# variables and expressions into predefined string 
#template
#this allows for the construction of flexible 
# and informative output based on changing data

# string formatting can be done using two methods
# 1) using the format() function
# 2) using f-strings

# 1) using the format() function 
name = "Rahul"
age = 25
text = "My name is {} and I am {} years old".format(name,age)
print(text)

# this was done using positional placeholder

# we can also use the named placeholders
text1 = "Name: {n},Age: {a}".format(n = "Bob",a = 30)
print(text1)

# 2) using the f-strings

name1 = "Siddhi"
age1 = 19
text2 = f"My name is {name1} and I am {age1} years old"
print(text2)