def trapping_rain_water(arr):

    max_units = 0

    for i in range(len(arr)):
        max_left = arr[i]
        j = 0
        while(j < i):
            if arr[j] > max_left:
                max_left = arr[j]
            j += 1

        max_right = arr[i]
        k = i + 1
        while(k < len(arr)):
            if arr[k] > max_right:
                max_right = arr[k]
            k += 1

        max_units += (min(max_right, max_left) - arr[i])

    return max_units


print(trapping_rain_water([2,0,2]))
print(trapping_rain_water([3,0,2,0,4]))
print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))