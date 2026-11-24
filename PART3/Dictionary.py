# Dictionary is an unordered,mutable collection of key-value pairs

my_dict = {
    "name":"siddhi",
    "age":"19",
    "city":"Jaipur"
}

print(my_dict["name"])

#Dictionary Methods
print(my_dict.keys())  #returns all keys
print(my_dict.values())  #return all values
print(my_dict.items()) #returns key-value pairs as tuples

print(my_dict.get("cgpa")) #return None as no such key as cgpa
# get(key) => a safer way to access value of a particular key.
#Instead of throwing an error it returns None if key doesn't exist

new_item = {"cgpa":9.8}
print(my_dict.update(new_item))
print(my_dict)

#LOOPS ON DICTIONARY
for key,value in my_dict.items():
    print(key,value)
