# 2.Write a function that takes a 2-dimensional NumPy array and returns the transpose of the array.
#     • Array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     • Output = [[1 4 7][2 5 8][3 6 9]]

# 3.Write a function that takes a 2-dimensional NumPy array as an argument and returns the sum of the elements along the first axis (rows).
#     • Array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     • Output = [12 15 18]

import numpy as np

def arrayy(x):
    return print("transporse array : \n",x.transpose())

def sumOfFirstExis(x):
    return print("Sum of First Element : \n",np.sum(x,axis=0))

n_rows = int(input("Enter number of rows: "))
n_cols = int(input("Enter number of columns: "))

arr = np.array([[int(input("Enter value for {}. row and {}. column: ".format(r + 1, c + 1))) for c in range(n_cols)] for r in range(n_rows)])

print("simple array : \n",arr)
arrayy(arr)

sumOfFirstExis(arr)