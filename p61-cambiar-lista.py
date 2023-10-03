# Cambiar los elementos de una lista 
import os
os.system("cls")

nums = [10.0, 9.0, 8.5, 6.5, 9.8, 7.0, 5.0, 6.2, 9.5]

print(nums, len(nums))
print(type(nums))
nums[0] = 7.0
nums[1] = 7.0
print(nums)
nums[2:5] = [9.0,9.0,9.0]
print(nums)
nums[-1] = 6.0
print(nums)
nums[6] = nums[6] + 5.0
print(nums)