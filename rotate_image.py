"""
Given a nxn 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
Sample Input and Output:
[[1,2,3],      [[7,4,1],
 [4,5,6],  ==>  [8,5,2],
 [7,8,9]]       [9,6,3]]
"""

def rotate_image(image):

    #step 1: transpose the image
    for i in range(len(image)):
        for j in range(i, len(image[i])):
            image[i][j], image[j][i] = image[j][i], image[i][j]


    #step 2: mirror  the image
    for i in range(len(image)):
        for j in range(len(image)//2):
            image[i][j], image[i][len(image) - 1 - j] = image[i][len(image) - 1 - j], image[i][j]

    return image


arr1 = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_image(arr1))
arr2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# output should be: [[13,9,5,1], [14,10,6,2], [15,11,7,3], []16,12,8,4]
print(rotate_image(arr2))