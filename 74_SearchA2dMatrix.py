class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b = 0
        t = len(matrix) - 1
        while b <= t:
            m = (b + t) // 2
            if matrix[m][0] == target: return True
            elif matrix[m][0] > target:
                t = m - 1
            elif matrix[m][0] < target:
                L = 0
                R = len(matrix[m]) - 1
                while L <= R:
                    row_mid = int((L + R) / 2)
                    if matrix[m][row_mid] == target: return True
                    elif matrix[m][row_mid] < target:
                        L = row_mid + 1
                    else: R = row_mid - 1
                b = m + 1
        return False
