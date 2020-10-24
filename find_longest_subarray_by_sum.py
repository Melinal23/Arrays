"""

Return the boundaries of the longest subarray.

Examples:
Input: arr=[1,2,3,7,5], s=12
Output: [2,4], because 2+3+7 = 12; [7,5] also equals 12 but is shorter

Input: arr=[1,2,3,4,5,6,7,8,9,10], s=15
Output: r = [1,5] because 1+2+3+4+5 = 15
"""

def find_longest_subarray_by_sum(arr,s):

    r = [-1]
    curr_sum = 0
    left = 0
    right = 0
    max_length = 0

    while(right < len(arr)):

        curr_sum += arr[right] #update curr sum

        while(left < right and curr_sum > s): # shrink window from the left
            curr_sum -= arr[left]
            left += 1

        curr_len = right - left
        if curr_sum == s and curr_len > max_length:
            max_length = curr_len
            r = [left+1,right+1]

        right += 1

    return r

"""
Time Complexity: O(n) where n is the number of elements in the input array
Space Complexity: O(1) no extra space user
"""

print(find_longest_subarray_by_sum([1,2,3,7,5], 12))
print(find_longest_subarray_by_sum([1,2,3,4,5,6,7,8,9,10], 15))
print(find_longest_subarray_by_sum([1,2,3,4,5,0,0,0,6,7,8,9,10], 15))