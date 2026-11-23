#Tuples = A tuple in python is ordered,immutable
#collection of items

tup = (10,20,30)
print(tup)
print(type(tup))  #<class 'tuple'>
empty_tuple = ()
single_element_tuple = (42,)

#Tuple characterstics
#ordered,immutable,allows duplicates,heterogenous

#rest of the things like indexing,slicing and loops in tuples are same as strings


#Tuples Methods

print(tup.index(20))  #returns index of first occurence for any val
print(tup.count(20))  #returns total count of occurence for any val


