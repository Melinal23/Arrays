"""
Given two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of
numbers, where one number is taken from a and the other from b, that can be added together to get a sum
of v. Return true if such a pair exists, otherwise return False.
"""

def sum_of_two(a, b, v):

    complements = set()

    for val in a:
        complements.add(v-val) #calculate the compliment

    for val in b:
        if val in complements:
            return True

    return False

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

print(sum_of_two([0,0,-5,30212], [-10,40,-3,9], -8))
print(sum_of_two([1,2,3], [10,20,30,40], 42))
print(sum_of_two([1,2,3], [10,20,30,40], 7))

"""
Given an array of ints that is already sorted in ascending order, find two number such that
they add up to a specific target number. 

The function should return indices of the two numbers such that they add up to the target.

Example:
Input => [2,7,11,15], target = 9
Output => [1,2]
"""


def two_sum_II(numbers, target):

    start = 0
    end = len(numbers) - 1

    while(start <= end):

        sum = numbers[start] + numbers[end]
        
        if sum < target:
            start += 1
        elif sum > target:
            end -= 1
        else:                           # they are equal
            return [start + 1, end + 1]
