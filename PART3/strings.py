#strings in python is a sequence of characters enclosed in quotes
#strings are immutable,means once created can't be changed

str1 = "hello world"
str2 = "Prime"

#length function
print(len(str2))   #5
#Concatenation
word1 = "Siddhi"
word2 = "Mudgal"

word = word1+" "+word2
print(word)

#loops on strings
s = "Python"
for ch in s:
    print(ch)

#ch will store individual chars - 'P','y','t' and so on

#Indexing in strings


#Indexing in strings
#Python follows zero besed indexing
s1 = "Python"
print(s[0]) #p
print(s[3]) #h
print(s[-1]) #n (negative index:last character)