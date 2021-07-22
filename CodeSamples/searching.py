# searching.py
# Python 3.9.5

# EXAMPLES ON HOW TO SEARCH FOR A TAREGET VALUE IN A NP ARRAY

import numpy as np


def my_search(a, x, eps):
    """Searches for a value within an array

    :param a: ndarray
    :param x: target value to be searched in the a
    :param eps: tolerance defining how close two floating point
    values must be in order to be considered equal.
    :return: cell index of the first occurrence of the target, or
    -1 if the target value is not found.
    """
    for i in range(len(a)):
        # isclose() compares two values and returns True if the
        # values are within eps (epsilon) of each other
        if np.isclose(a[i], x, eps):
            return i
    return -1


# =====

print("\nBegin array search demo \n")

arr = np.array([7.0, 9.0, 5.0, 1.0, 5.0, 8.0])

print("Array arr is ")
print(arr)
print("")

target = 5.0
print("Target value is ")
print(target)
print("")

found = target in arr
print(f"Search result using 'target in arr' syntax = {found}")
print("")

# where() returns a tuple containing an array. The array
# holds the indices in the searched array where the target values occurs.
# If there is no such value, the return result is a tuple with an
# array with lenght 0
result = np.where(arr == target)
print("Search result using np.where(arr == target) is ")
print(result)  # (array([2, 4], dtype=int64,)
print("")

idx = my_search(arr, target, 1.0e-6)
print("Search result using my_search() = ")
print(idx)
print("")

print("\nEnd demo \n")
