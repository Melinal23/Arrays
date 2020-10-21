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
