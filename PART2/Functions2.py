# Functions with parameters 
# we can also pass data to a function using parameters
# (inside parentheses),values actually passed when 
#calling the functions are called arguments.
def sum(a,b):
    print(a+b)

#calling the function and passing the arguments
sum(5,10)

#Fnx to compute average of 3 numbers 
def avg(a,b,c):
    return (a+b+c)/3
print(avg(2,3,4))

#Default parameters 
#sum() - fnx with default param 1 
def sum(a,b = 1): #default val of b is 1
    return a+b 
print((sum(5)))  #sum = 6

# the above functions that we have created are the user defined functions
# and we can also create built in functions 
# that are print(),input(),type(),range()

