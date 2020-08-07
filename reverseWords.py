def reverseWords(array):

    # base case

    if len(array) == 0:
        return []

    #reverse the entire array

    start = 0
    end = len(array) - 1

    while start <= end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    #reverse the words

    i = 0
    j = 0

    while i < len(array) and j < len(array):

        while j < len(array) and array[j] != " ":
            j  += 1

        i_temp = i
        j_temp = j-1

        while i_temp <= j_temp:
            array[i_temp], array[j_temp] = array[j_temp], array[i_temp]
            i_temp += 1
            j_temp -= 1


        i = j = (j + 1)


    return "".join(array)

array = ['c', 'a', 'k', 'e', ' ',
         'p', 'o', 'u', 'n', 'd', ' ',
         's', 't', 'e', 'a', 'l']

array1 = ['t','h','e','r','e',' ', 'h', 'i']

print(reverseWords(array))

def reverseWords1(array):
    pass
