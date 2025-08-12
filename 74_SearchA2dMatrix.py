class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b = 0
        t = len(matrix) - 1
        while b <= t:
            m = (b + t) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                t = m - 1
            elif matrix[m][0] < target:
                if target in matrix[m]: return True
                else:
                    b = m + 1
        return False
