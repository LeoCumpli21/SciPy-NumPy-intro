# arrays.py
# Python 3.9.5

# EXAMPLES ON HOW TO CREATE NP ARRAYS

import numpy as np


def my_print(arr, cols, dec):
    # print array using indexing
    n = len(arr)  # n = arr.size
    fmt = "%." + str(dec) + "f"  # like %.4f
    for i in range(n):  # alt: for x in arr
        if i > 0 and i % cols == 0:
            print("")
        print(fmt % arr[i], end=" ")
    print("\n")


def my_odds(n):
    """Makes a np array with the first n odd integers

    :param n: integer
    :return ndarray: an array conformed by the first n odd integers
    """
    result = np.zeros(n, dtype=np.int32)
    val = 1
    for i in range(n):
        result[i] = val
        val += 2
    return result


# =====

print("\nBegin array demo \n")

print("Creating array arr using np.array() and list with hard-coded values ")
arr = np.array([1.0, 3.0, 5.0, 7.0, 9.0])  # float64
dt = np.dtype(arr[0])
print("Cell element type is " + str(dt.name))
print("")

print("Printing array arr using built-in print() ")
print(arr)
print("")

print("Creating int array arr using np.arange(9) ")
arr = np.arange(9)  # [0, 1, . . 8] # int32
print("Printing array arr using built-in print() ")
print(arr)
print("")

cols = 4
dec = 0
print(f"Printing array arr using my_print() with cols= {cols} and dec= {dec}")
my_print(arr, cols, dec)

print("Creating array arr using np.zeros(5) ")
arr = np.zeros(5, dtype=np.int32)  # default value is float64
# ones() np function initializes an array to all 1.0 values.
print("Printing array arr using built-in print() ")
print(arr)
print("")

print("Creating array arr using  np.linspace(2., 5., 6)")
# linespace(start, stop, num) returns array with values evenly spaced
# stop param is inclusive.
arr = np.linspace(2.0, 5.0, 6)  # 6 values from [2.0 to 5.0] inc.
print("Printing array arr using built-in print() ")
print(arr)
print("")

print("\nEnd demo \n")
