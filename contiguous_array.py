"""
Given a binary array, find the max length of a contiguous sub-array with equal number of 0 and 1.
"""

def contiguous_array(arr):


    counts = {}
    counts[0] = -1
    count = 0
    max_length = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            count -= 1
        elif arr[i] == 1:
            count += 1

        if count in counts:
            max_length = max(max_length, i - counts[count])
        else:
            counts[count] = i #store count


    return max_length

"""
Time Complexity: O(n) where n is the elements in arr
Space Complexity: O(n) where n is the elements in arr
"""

print(contiguous_array([0,1])) # 2
print(contiguous_array([0,1,0])) # 2
print(contiguous_array([0,1,0,1,0,1,1,0,0]))
print(contiguous_array([1,0,1])) # 2
print(contiguous_array([1,1,1,0,0,1,1])) # 4
