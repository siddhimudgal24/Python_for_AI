nums = [5,2,9]
print(len(nums))  #3

nums.append(7)
print(nums)   #[5,2,9,7]

nums.insert(1,4)
print(nums)  #[5,4,2,9,7]

nums.sort()
print(nums) #[2,3,5,7,9]

nums.reverse()
print(nums)  #[9,7,5,4,2]