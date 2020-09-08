def twoSum(nums, target):
    
    for i in range(len(nums)):
        if target - nums[i] in nums and nums.index(target - nums[i]) != i:
            return [i, nums.index(target - nums[i])]
        
"""
Time Complexity: O(n^2) because of the for loop and the "in" operator
Space Complexity: O(1) no extra space being used
"""
