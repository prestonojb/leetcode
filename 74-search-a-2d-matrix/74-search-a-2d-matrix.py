class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #  Exists in row
        top, bot = 0, len(matrix) - 1
        
        while top <= bot:
            row = (top + bot) // 2

            l, r = 0, len(matrix[0]) - 1

            while l <= r:
                m = (l+r) // 2
                if matrix[row][m] == target:
                    return True
                elif matrix[row][m] < target:
                    l = m + 1
                else:
                    r = m - 1

            if l == 0:
                bot = row - 1
            elif r == len(matrix[0]) - 1:
                top = row + 1
            else:
                return False
        
        return False