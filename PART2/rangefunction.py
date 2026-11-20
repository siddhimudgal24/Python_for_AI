#range function in python is used to generate a 
#sequence of numbers, typically for use in loops
#range function has 3 parameters
#start(default =0)
#stop(the number to stop before),stop is not included in this
#step (default = 1), how much to increase by each time

#single argument - stop

for i in range(5):
    print(i)

#output = 0,1,2,3,4

#2 arguments - start,stop
for i in range(1,6):
    print(i)

#output: 1,2,3,4,5

#3 arguments - start,stop,step

for i in range(1,10,2):
    print(i)

#output: 1,3,5,7,9
