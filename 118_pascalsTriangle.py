from typing import List
'''
first cell is one
second cell is one, one (1 + 0)?
first and last element of every row is one
cell (3, 2) == sum(cell(2,1), cell(2,2))
cell (4,2) = sum(cell(3,1), cell(3,2))
cell (4,3) = sum(cell(3,2), cell(3,3))
add the values of two cells from the row above current row:
    the cell to the left of the current cell (i = cur_i - 1)
    the cell to the right of the current cell (i = cur_i)
    if one of the cells does not exist, treat it as 0

1|       1
2|   1       1
3|  1 (1 + 1) 1 n -1 
4| 1 (1 + 1 + 1) (1 + 1 + 1) 1 n - 1
5| 1 (1 + 1 + 1 +) (2 * (1+1+1)) (1 + 1 + 1+ 1) 1 n -1, 2*n-2
6| 1 5 10 10 5 1 n - 1 (2 * )
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row in range(1, numRows + 1):
            cur_row = []
            for cell in range(row):
                if cell in set((0, row - 1)):
                    cur_row.append(1)
                else:
                    cur_row.append(prev_row[cell - 1] + prev_row[cell])
            prev_row = cur_row
            res.append(cur_row)
        return res
