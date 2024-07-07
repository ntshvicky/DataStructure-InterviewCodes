# Problem: Maximum Subarray Sum (Kadane’s Algorithm)
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

nums = [-2,1,-3,4,-1,2,1,-5,4]

# Function to find the maximum subarray sum
def max_subarray_sum(nums):
    max_current = nums[0]
    max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Calling the function and printing the result
result = max_subarray_sum(nums)
print(result)  # Output: 6
