# matrices.py
# Python 3.9.5

# Matrices are arguably the most important data structure in
# numeric and scientific programming

import numpy as np


def show_matrix(m, dec, wid):
    fmt = "%" + str(wid) + "." + str(dec) + "f"
    # shape() returns a tuple (#rows, #cols)
    (rows, cols) = np.shape(m)
    for i in range(rows):
        for j in range(cols):
            print(fmt % m[i, j], end=" ")
        print("")  # end of row
    print("")  # final newline


# =====

print("\nBegin matrices demo \n")

ma = np.matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  # 2x3

# mb is a NumPy n-dimensional array rather than a np amtrix
mb = np.zeros((3, 2), dtype=np.int32)  # 3x2

mc = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  # 2x3

# Matrices with one row are called row matrices
md = np.matrix([[7.0, 8.0, 9.0]])  # 1x3
# Matrices with one column are called column matrices.
me = np.matrix([[7.0], [8.0], [9.0]])

# You can create a column matrix form a row matrix (or vice versa)
# using the reshape() function.
mf = np.reshape(me, (1, 3))

# Ypu can make a regular array form an ndarray-style matrix with:
am = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  # 2x3 ndarray matrix
arr = np.ravel(am)  # same as above

print("Matrix ma is ")
print(ma)
print("")

print("Matrix mb is ")
print(mb)
print("")

print("N-dimensional array/matrix mc is ")
print(mc)
print("")

print(f"Matrix mf: \n{mf} \nis a reshaped version of matrix me: \n{me}", end="\n\n")
print(
    f"""Matrix am: \n{am} \nis a ndarray matrix.
Array arr: \n{arr} \nis a regular array that was made by flattening Matrix am""",
    end="\n\n",
)

print("ma is type " + str(type(ma)))
print("mb is type " + str(type(mb)))
print("mc is type " + str(type(mc)))
print("")

print("Contents of matrix ma using show_matrix(ma, 3, 6) are ")
show_matrix(ma, 3, 6)

msum = ma + mc
print("Result of ma + mc = ")
print(msum)
print("")

md = np.matrix([[7.0, 8.0, 9.0]])
# broadcasting:
mx = ma + md
# ma is 2x3 and md is 1x3. NumPy expands md to a 2x3 matrix
# duplicating values so  that it has the same shape as ma
print("Matrix md is ")
print(md)
print("")
print("Result of ma + md is ")
print(mx)

print("\nEnd demo \n")
