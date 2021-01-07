import numpy as np

val = [[1, 2, 3, 4],
       [5, 6, 7, 0],
       [8, 9, 0, 0],
       [10, 0, 0, 0]]
arr = np.array([[1, 2, 3, 4],[5, 6, 7, 0],[8, 9, 0, 0],[10, 0, 0, 0]])
print("Smallest element in the matrix : ",arr.min())
print("Biggest element in the matrix : ",arr.max())
print("Sum of the elements of the matrix : ",np.sum(val))
