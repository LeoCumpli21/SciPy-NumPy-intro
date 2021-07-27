# determinants.py
# Python 3.9.5

# The determinant of a matrix is a value that indicates
# whether or not the matrix has an inverse.
# They only apply to square matrices
# Matrices that have a determinant of 0 do not have an
# inverse

import numpy as np


def extract(m, col):
    # return n-1 x n-1 submatrix w/o row 0 and col
    n = len(m)
    result = np.zeros((n - 1, n - 1))
    for i in range(1, n):
        k = 0
        for j in range(n):
            if j != col:
                result[i - 1, k] = m[i, j]
                k += 1
    return result


def my_det(m):
    # inefficient and recursive
    n = len(m)
    if n == 1:
        return m[0]
    elif n == 2:
        return (m[0, 0] * m[1, 1]) - (m[0, 1] * m[1, 0])
    else:
        sum = 0.0
        for k in range(n):
            sign = -1
            if k % 2 == 0:
                sign = +1
            subm = extract(m, k)
            sum = sum + sign * m[0, k] * my_det(subm)
        return sum


# =====

print("\nBegin matrix determinant demo \n")

m = np.matrix([[1.0, 4.0, 2.0, 3.0], [0.0, 1.0, 5.0, 4.0], [1.0, 0.0, 1.0, 0.0], [2.0, 3.0, 4.0, 1.0]])

print("Matrix m is ")
print(m)
print("")

d = np.linalg.det(m)
print("Determinant of m using np.linalg.det() is ")
print(d)
print("")

d = my_det(m)
print("Determinant of m using my_det() is ")
print(d)
print("")

print("\nEnd demo \n")
