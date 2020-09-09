def twoSum(nums, target):
    
    for i in range(len(nums)):
        if target - nums[i] in nums and nums.index(target - nums[i]) != i:
            return [i, nums.index(target - nums[i])]
        
"""
Time Complexity: O(n^2) because of the for loop and the "in" operator
Space Complexity: O(1) no extra space being used
"""

def two_sum_optimized(nums, target):

    elements = {}

    for i in range(len(nums)):
        if nums[i] not in elements:
            elements[nums[i]] = [i,1]  # store element in dictionary with its index
        elements[nums[i]][-1] += 1     # increment times appears

        temp = target-nums[i]
        vals = elements.get(temp)

        #if compliment num in dict and index is not the same and times it appears is not zero
        if vals and vals[0] != i and vals[-1] > 1:
            return sorted([i, vals[0]])
        
"""
Time Complexity: O(n) because of the for loop
Space Complexity: O(n) because of dictionary storing values
"""      
