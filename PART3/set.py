#Set is an unordered collection of unique elements
my_set = {1,2,2,3,3,4,5}
print(my_set)  #{1,2,3,4,5}
print(type(my_set))
print(len(my_set))   #5

empty_set = set()

#set characterstics
#sets can only have unique elements
# they are unordered - no indexing or slicing
# They are mutable - can add or remove elements
# set elements must be immutable (like strings,numbers,tuples)
# sets are often used when we need uniqueness or mathematical set operations

#set methods
s = {10,20,30}

s.add(40) #{10,20,30,40}
print(s)

s.remove(10) #{20,30,40}
print(s)

print(s.pop())  #can be any value

s.clear()
print(s)    #set()- empty set


#union and intersection
A = {1,2,3}
B = {3,4,5}

print(A.union(B))   #{1,2,3,4,5}
print(A.intersection(B))  #{3}