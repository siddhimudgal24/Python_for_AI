numbers = [5,12,7,3,18,9]
x = 18
idx = 0
target = int(input("Enter the target value that you want to search"))

for num in numbers:
    if num == target:
        print(f"{x} found at index = {idx}")
        break
    idx+=1