"""
need to check if each row contains 1 ...n
need to check if each column contains 1 ...n
this cannot be true if any duplicates exist in the row/column
each row has n elements
each column has n elements
how to solve this by going through the matrix right to left and top to bottom?
use a hashmap. if any value exceeds n, return false
I made 2 n x n matrices, one to keep track of the rows and
one to keep track of the cols. the indexes represent the values in the
original matrix. if any item in these lists is greater than 1, it means
a value was duplicated in the row/column of the original matrix, and
therefore it could not possibly contain all values.
loop through the matrix:
for y in range(0,n):
    for x in range(0,n):
        value = matrix[y][x]
        counts[value - 1] += 1
"""


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = [[0] * n for _ in range(n)]
        cols = [[0] * n for _ in range(n)]
        for y in range(n):
            for x in range(n):
                value = matrix[y][x]  # yth row, xth column
                index = value - 1
                rows[y][index] += 1
                cols[x][index] += 1
                if rows[y][index] > 1 or cols[x][index] > 1:
                    return False
        return True

