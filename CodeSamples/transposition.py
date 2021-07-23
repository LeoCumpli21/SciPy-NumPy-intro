# transposition.py
# Python 3.9.5

# The NumPy library supports three built-in ways to transpose
# a matrix m: the m.transpose() function, the np.transpose(m) function,
# and the m.T property.

import numpy as np


def my_transpose(m):
    (rows, cols) = np.shape(m)
    result = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            result[j, i] = m[i, j]
    return result


# =====

print("\nBegin matrix transposition demo \n")

m = np.matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])

print("Matrix m = ")
print(m)
print("")

mt = m.transpose()
print("Transpose from m.transpose() function = ")
print(mt)
print("")

mt = np.transpose(m)
print("Transpose from np.transpose(m) function = ")
print(mt)
print("")

mt = m.T
print("Transpose from m.T property  = ")
print(mt)
print("")

mt = my_transpose(m)
print("Transpose from my_transpose() function = ")
print(mt)
print("")

print("\nEnd demo \n")
