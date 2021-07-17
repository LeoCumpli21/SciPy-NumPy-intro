# structure.py
# Python 3.9.5

import numpy as np


def make_x(n):
    """Accepts a matrix dimension parameter n and returns a matrix
    where the major and minor diagonals have 1.0 values, and 0.0
    values elsewhere

    :param n: An odd integer
    :return ndarray: A NumPy matrix with 1.0 values on the main
    and minor diagonals, and 0.0 values elsewhere
    """

    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j or (i + j == n - 1):
                result[i, j] = 1.0
    return result


def main():
    print("Begin program structure demo")

    try:
        n = 5
        print(f"X matrix with size n = {n} is ")
        mx = make_x(n)
        print(mx)

        n = -1
        print(f"X matrix with size n = {n} is ", end="")
        mx = make_x(n)
        print(mx)
    except Exception as e:
        print(f"Error: {e}")

    print("End demo")


if __name__ == "__main__":
    main()
