def smallestSubarray(array):

    first_index = 0
    second_index = len(array) -1

    while(first_index < len(array)-1 and array[first_index] <= array[first_index+1]):
        first_index += 1

    if first_index == len(array)-1:  #the array is sorted
        return 0

    while(second_index > 0 and array[second_index] >= array[second_index - 1]):
        second_index -= 1

    local_min = min(array[first_index:second_index+1])
    local_max = max(array[first_index:second_index+1])


    while first_index > 0 and array[first_index -1 ] > local_min:
        first_index -=1

    while second_index < len(array)-1 and array[second_index + 1] < local_max:
        second_index -= 1


    return second_index - first_index + 1



print(smallestSubarray([1,2,3]))