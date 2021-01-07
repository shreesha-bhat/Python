import numpy as np

val = [[1, 2, 3, 4, 5],
       [5, 1, 2, 3, 4],
       [4, 5, 1, 2, 3],
       [3, 4, 5, 1, 2],
       [2, 3, 4, 5, 1]]

array = np.array([[1, 2, 3, 4, 5],[5, 1, 2, 3, 4],[4, 5, 1, 2, 3],[3, 4, 5, 1, 2],[2, 3, 4, 5, 1]])
print("Smallest element in the matrix : ",array.min())
print("Biggest element in the matrix : ",array.max())
print("Sum of the elements of the matrix : ",np.sum(val))
