"""
Given a square matrix of size NxN, calculate the absolute difference between the
sums of its diagonals.

The first line contains a single integer, N. The next  lines denote the matrix's
rows, with each line containing space-separated integers describing the columns.
"""

# 2D array

def l2r_diagonal(r):

    number = 0
    l2r = 0
    while number < len(r):
        a = list(r[number].split())
        l2r += int(a[number])
        number += 1
    return l2r


def r2l_diagonal(r):

    r.reverse()
    number = 0
    r2l = 0
    while number < len(r):
        a = list(r[number].split())
        r2l += int(a[number])
        number += 1
    return r2l


def diagonal_sum(left, right):
    print abs(left + right)


n = input('Please enter N, where N is the number of columns and rows of the matrix (NxN): ')
row = list()
# python operations: list, map, stack, heap, etc.. complexity
for rows in range(n):
    # string formatting
    row.append(raw_input('Enter values in row number ' + str(rows + 1) + " : "))

diagonal_sum(l2r_diagonal(row), r2l_diagonal(row))







