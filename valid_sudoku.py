'''
- iterate through every inner array once, keeping track of
- rows and columns as we go
- do not alter sets when cell == '.'
- don't need to know exact position of any element in its subgrid,
- just which subgrid it belongs to
- sub grids start at rows 0, 3, 6
- for i in board_len:
    in_row = set()
    in_col = set()
    for j in row_len:
        row_cell = board[i][j]
        col_cell = board[j][i]
        if row_cell in in_row or col_cell in in_col:
            return False
        in_row.add(row_cell)
        in_board.add(board_cell)
- if a row or column has
    - duplicates
- it is invalid
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subgrids = {n: set() for n in range(9)}
        col_sets = {n: set() for n in range(9)}
        n = len(board)
        for r in range(n):
            row_set = set()
            for c in range(n):
                subgrid = r//3*3+c//3
                row_cell = board[r][c]
                cell_column = c
                if (row_cell in row_set or
                    row_cell in col_sets[c] or
                    row_cell in subgrids[subgrid]):
                    return False
                elif row_cell != ".":
                    row_set.add(row_cell)
                    col_sets[c].add(row_cell)
                    subgrids[subgrid].add(row_cell)
        return True

# Second time solving this problem, this time in python.
# I still struggled with how to handle the subgrids,
# And I suspect this solution is highly memory inefficient
# but progress is progress.
