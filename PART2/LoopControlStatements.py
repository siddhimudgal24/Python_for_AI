# LOOP CONTROL STATEMENTS = BREAK AND CONTINUE
# the break keyword stops the loop immediately

# Break for multiple of 6
i = 1
while i<=10:
    if(i%6==0):
        break
    print(i)
    i+=1

# OUTPUT = 1,2,3,4,5

# The continue Keyword 
# it skips the rest of the current iteration and moves to the next one
# skip multiples of 3
print("Example of continue keyword")
i =0
while(i<10):
    i+=1
    if(i % 3 ==0):
        continue;
    print(i)

#Output = 1,2,4,5,7,8,10