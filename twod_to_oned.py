"""UMPIRE:
# U - Are we suppose to return the 1D array?
#   - Are the elements in in the 2D array always going to be integers
    - Empty array?
    - One element in array?
    - Do we know the number of rows/columns in advance?

  - what does our 2d array look like? ex:
  2darr = [[1,2,3], [4,5,6]] -> 1darr = [1,2,3,4,5,6]
  2darr = 1 2 3       ->      1darr = 1 2 3 4 5 6
          4 5 6

 M - use the formulas given to us in lecture, and use the spiral problem as a reference
# P - 1D array index = rowIndex * noOfCols + colIndex
#
"""
def twod_to_oned(twod_array):

  if len(twod_array) == 0:
    return []

  # 1 elem: [[1,2,3]] or [[1]]

  num_rows = len(twod_array)
  num_cols = len(twod_array[0])

  oned_array = [0] * (num_rows * num_cols)

  for row in range(len(twod_array)):
    for col in range(len(twod_array[row])):
      oned_array[row * num_cols + col] = twod_array[row][col]


  return oned_array

print(twod_to_oned([[1,2,3],
 [4,5,6]]))

print(twod_to_oned([[11, 12, 5, 2], [15, 6, 10, 23], [10, 8, 12, 5], [12, 15, 8, 6]]))

print(twod_to_oned([[1,2,3], [4,5,6]]))

print(twod_to_oned([[]]))

print(twod_to_oned([[1]]))

print(twod_to_oned([[1, 2, 3]]))

def paulinas_soln(array):
  if len(array) == 0:
      return []

  num_rows = len(array)
  num_cols = len(array[0])

  

