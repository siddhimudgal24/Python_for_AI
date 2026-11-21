#count vowels in a word (using for)
word = input("Enter the word here:")
count = 0
for ch in word:
    if (ch =='a' or ch =='e' or ch == 'i' or ch == 'o' or ch=='u'):
        count+=1

print("No. of vowels in the word you have Entered:",count)