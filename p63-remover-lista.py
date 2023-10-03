# Remover elementos de la lista
import os
os.system("cls")
nums = [1.3,5,7,9,11,99,15,88,19,100]

print(nums, len(nums))
nums.remove(99)
print(nums, len(nums))
nums.pop(8)
print(nums, len(nums))
nums.pop()
print(nums, len(nums))
nums.clear()
print(nums, len(nums))
