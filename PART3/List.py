# A list is a collection of items in Python
# Items in list are orderded, changeable(mutable)
# and can contain duplicates.
# List can hold any data type: numbers,strings,other lists,etc
# List are written using square brackets[]

my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))    #<class 'list>

my_list2 = {10,"Hello",3.14,True,10}  # Heterogenous List
print(my_list2)


#List characterstics
# 1) Ordered,Mutable,Allows Duplicates,Heterogenous

#List Indexing
#Access Elements

fruits = ["apple","banana","cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Modify Elements 

my_list1 = [1,2,3,4]
my_list1[0] = 10
print(my_list1) #[10,2,3,4]