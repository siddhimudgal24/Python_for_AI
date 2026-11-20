#range function in python is used to generate a 
#sequence of numbers, typically for use in loops
#range function has 3 parameters
#start(default =0)
#stop(the number to stop before),stop is not included in this
#step (default = 1), how much to increase by each time

#single argument - stop
print("using single argumnet")
for i in range(5):
    print(i)

#output = 0,1,2,3,4

#2 arguments - start,stop
print("using two argumnets")
for i in range(1,6):
    print(i)

#output: 1,2,3,4,5

#3 arguments - start,stop,step
print("using three argumnets")
for i in range(1,10,2):
    print(i)

#output: 1,3,5,7,9
