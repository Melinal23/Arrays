"""
Given an array nums of n integers where n > 1, return an array output such that output[i] is equal
to the product of all the elements of nums except nums[i]

[1,2,3,4] --> VALID [24,12,8,6]
[1] --> invalid
[] --> invalid
[-5,2,-4] --> VALID
"""

def product_except_itself_1(nums):

    output = [0] * len(nums)
    left_products = [0] * len(nums)
    right_products = [0] * len(nums)
    left_products[0] = 1 # initialize to 1 because there is nothing to the left of 1st element
    right_products[-1] = 1 # initialize to 1 bec there is nothing to the right of last element

    for i in range(1, len(nums)):
        left_products[i] = nums[i-1] * left_products[i-1]

    for i in range(len(nums)-2, -1, -1):
        right_products[i] = nums[i+1] * right_products[i+1]

    for i in range(len(nums)):
        output[i] = left_products[i] * right_products[i]

    return output

"""
Time Complexity: O(n) where n is the num of elements in nums
Space Complexity: O(n) for left and right products
"""

print(product_except_itself_1([1,2,3,4]))

def product_except_itself_2(nums):

    output = [0] * len(nums)
    output[0] = 1 # initialize to 1 because there is nothing to the left of 1st element
    R = 1

    for i in range(1, len(nums)):
        output[i] = nums[i-1] * output[i-1]

    for i in range(len(nums)-1, -1, -1):
        output[i] = R * output[i]
        R = R * nums[i]

    return output

"""
Time Complexity: O(n) where n is the num of elements in nums
Space Complexity: O(1) if output array does not count
"""

print(product_except_itself_2([1,2,3,4]))

