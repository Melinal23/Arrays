def twoSum(numbers, target):

    for i in range(len(numbers)):
        temp = target - numbers[i]
        find_temp = binary_search(numbers, temp, i+1)

        if(find_temp != i and find_temp != -1):
            return [i + 1, find_temp + 1]


def binary_search(numbers, temp, i):

    start = i
    end = len(numbers) - 1

    while(start <= end):

        mid = (start + end) // 2

        if numbers[mid] > temp:
            end = mid - 1
        elif numbers[mid] < temp:
            start = mid + 1
        else:
            return mid

    return -1
                
"""
Time Complexity: O(n*logn) because of the binary search implementation over the entire array (n comes from for loop, logn from binary search)
Space Complexity: O(1) because no extra space is being used
"""
 
def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1

    while(start < end):
        sum = numbers[start] + numbers[end]

        if sum > target:
            end -= 1
        elif sum < target:
            start += 1
        elif sum == target:
            return [start + 1, end + 1]

"""
Time Complexity: O(n) iteration over the entire array
Space Complexity: O(1) because no extra space is being used
"""
