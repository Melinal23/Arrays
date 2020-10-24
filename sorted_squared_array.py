"""
You have a sorted array integers. Write a function that returns a sorted array containing the squares of those
integers.

Numbers in the input array can be negative

Examples:
[-7,-3,-1,4,8,12] ==> [1,9,16,49,64,144]
[1,2,3] ==> [1,4,9]
[-3,-2,-1] ==> [1,4,9]
[] ==> invalid input
[-6,-4,-1,2,3,5]
"""

def sorted_squared_array(arr):

    output = [0] * len(arr)

    start = 0
    end = len(arr)-1
    output_index = end

    while(start <= end):

        t1 = arr[start] * arr[start]
        t2 = arr[end] * arr[end]

        # insert the bigger squared value at the end of the output array
        if t1 > t2:
            output[output_index] = t1
            start += 1
        else:
            output[output_index] = t2
            end -= 1

        output_index -=1

    return output

"""
Time Complexity: O(n) where n is the number of elements in the input array
Space Complexity: O(1) no extra space used
"""

print(sorted_squared_array([1,2,3]))
print(sorted_squared_array([-3,-2,-1]))
print(sorted_squared_array([-7,-3,-1,4,8,12]))
print(sorted_squared_array([-6,-4,-1,2,3,5]))

