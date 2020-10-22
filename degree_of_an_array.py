"""
Given a non-empty array of non-negative integers nums the degree of this array is defined as the maximum freq
of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same
degree as nums.
"""

def degree_of_array(arr):

    items = {}
    first_seen = {}
    degree = 0
    min_length = 0

    for i in range(len(arr)): #store item starting position and count
        if arr[i] not in items:
            first_seen[arr[i]] = i

        if arr[i] not in items:
            items[arr[i]] = 1
        else:
            items[arr[i]] += 1

        if items[arr[i]] > degree: #update the degree
            degree = items[arr[i]]
            min_length = i - first_seen[arr[i]] + 1
        elif items[arr[i]] == degree:
            min_length = min(min_length, i - first_seen[arr[i]] + 1)

    return min_length


"""
Time Complexity: O(n) because we are looped through every element in arr (n total)
Space Complexity: O(n) due to the dictionaries we use, can hold all elements in arr
"""


print(degree_of_array([1,2,2,3,1]))
print(degree_of_array([1,2,2,3,1,4,2]))

