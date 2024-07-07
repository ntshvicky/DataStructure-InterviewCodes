# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [2, 7, 11, 15]
target = 9

# Function to find the two indices
def two_sum(nums, target):
    num_to_index = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

# Calling the function and printing the result
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
