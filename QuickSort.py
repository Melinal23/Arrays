"""
Average case complexity is O(n * log n)
Worst-case complexity is O(n^2)

Strategies to picking pivot:

1) Pick the first element in the array
2) Pick a random element
3) pick the median of three partitioning (start + end ) // 2
4)

Use insertion for smaller arrays, it is faster than quicksort

"""


#parkinson's
def quickSort(arr):
    quickSortHelper(arr, 0, len(arr)-1)

    return arr

def quickSortHelper(arr, start, end):

    if start < end:

        splitpoint = partition(arr,start,end)

        quickSortHelper(arr,splitpoint+1, end) #right side
        quickSortHelper(arr,start,splitpoint-1) #left side

def partition(arr, start, end):

    piv_Index = start
    pivotvalue = arr[piv_Index]

    # arr[start], arr[piv_Index] = arr[piv_Index], arr[start] #move pivot out of the way


    leftptr = start
    rightptr = end
    done = False

    while not done:

        while leftptr <= rightptr and arr[leftptr] <= pivotvalue:
            leftptr +=1

        while rightptr >= leftptr and arr[rightptr] >= pivotvalue:
            rightptr -=1

        if rightptr < leftptr:
            done = True
        else:
            #swap
            arr[leftptr], arr[rightptr] = arr[rightptr], arr[leftptr]

    #swap the pivot with the rightptr val
    arr[start], arr[rightptr] = arr[rightptr], arr[start]

    return rightptr #splitpoint

print(quickSort([7, 10, 4, 3, 20, 15]))
print(quickSort([7, 2, 4, 3, 0, 15]))


#kamila's
def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array [1:] if i <= pivot]
    greater = [i for i in array [1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quickSort([7, 10, 4, 3, 20, 15]))