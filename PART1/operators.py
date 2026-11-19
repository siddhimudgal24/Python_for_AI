# operators is a symbol that tells python to perform a specific computation on one or more values(called operands)
print(1+3) # "+" is an operator and (1,3) are operands
a = 5
b = 10

# Arithmetic Operators 
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiply
print(a/b) #division
print(a%b) #modulo - remainder
print(a**b) #power

#Relational Operators 
#equal to
print("a==b:",a==b) #False
# not equal to
print("a!=b:",a!=b) #True
#Greater than 
print("a>b:" ,a>b) #False
#Less than 
print("a<b:",a<b) #True
#Greater than or equal to
print("a>=b:",a>=b) #False
#Less than or equal to 
print("a<=b:",a<=b)#True

#Assignment operators
#Simple assignment 
x = 10
print("x = ",x) #10

x+=5 #equilvalent to x = x+5
print("x+=5 ->",x) #15

x-=3 # equilvalent to x = x-3
print("x-=3 ->",x) #12

x*=2 #equilvalent to x = x*2
print("x*=2 ->",x) #24

x/=4 # equilvalent to x/=4
print("x/=4 ->",x) #6.0

x%=4 #equivalent to x = x%4
print("x%=4 -> ",x) #2.0

x**=3 #equivalent to x = x**3
print("x**=3 ->" , x) # 8.0



#Logical operators => used to combine the boolean values
# we have 3 logical operators => and,or,not

p = 10
q = 20
r = 5

#AND 
print(p>r and q>p)  #True

#OR 
print(p>q or q>r) #True

#NOT
print(not(p>q)) #True


#unary operators
b = 5
c = -b
print(b) #5
print(c) #-5

