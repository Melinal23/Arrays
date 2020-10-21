"""
Given an integer array, in which the numbers in the array are valued between 1 and the length of the array,
find the first duplicate number for which the second occurrence has the minimal index.
"""

def first_duplicate_1(arr):

    seen = set()

    for item in arr:
        if item >= 1 and item <= len(arr):
            if item not in seen:
                seen.add(item)
            else:
                return item

    return -1

"""
Time Complexity: O(n) due to the for loop of the input array
Space Complexity: O(n) due to our set
"""

# print(first_duplicate_1([2,1,3,5,3,2]))
# print(first_duplicate_1([2,2]))

def first_duplicate_2(arr):

    for item in arr:
        if arr[abs(item) - 1] < 0: # if neg, it is a dup
            return abs(item)
        else:
            temp = arr[abs(item) - 1]
            arr[abs(item)-1] = -(temp)

    return -1

"""
Time Complexity: O(n) due to the for loop of the input array
Space Complexity: O(1)
"""

print(first_duplicate_1([2,1,3,5,3,2]))
print(first_duplicate_1([2,2]))
