def find_kth_smallest(array, k):

  array.sort()

  return array[k-1]


print(find_kth_smallest([7, 10, 4, 3, 20, 15],3) == 7)
print(find_kth_smallest([7, 10, 4, 3, 20, 15],4) == 10)




"""
Paulina's Solution
Time Complexity: O(N)
Space Complexity: O(1)
"""

def kth_smallest(arr: list, k: int) -> int:
    return quickSelect(arr, 0, len(arr) - 1, k)

def quickSelect(arr, left, right, n):
    if left == right:
        return arr[left]

    if arr == None or len(arr) < 1:
        return None
    part = partition(arr, left, right, n)

    if n == part + 1:
        return arr[part]
    elif n < part + 1:
        return quickSelect(arr, left, part-1, n)
    else:
        return quickSelect(arr, part+1, right, n - part)

def partition(arr, start, end, n):
    pivot = arr[end]
    follower = leader = start
    while leader < end:
        if arr[leader] <= pivot:
            arr[follower], arr[leader] = arr[leader], arr[follower]
            follower += 1
        leader += 1
    arr[follower], arr[end] = arr[end] , arr[follower]
    return follower