from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        row = len(matrix)
        col = len(matrix[0])

       
        self.prefix_Mat = [[0] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                
                top = self.prefix_Mat[i-1][j] if i > 0 else 0
                left = self.prefix_Mat[i][j-1] if j > 0 else 0
                top_left = self.prefix_Mat[i-1][j-1] if (i > 0 and j > 0) else 0

                self.prefix_Mat[i][j] = matrix[i][j] + top + left - top_left

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        last_corner = self.prefix_Mat[row2][col2]
        top_right = self.prefix_Mat[row1 - 1][col2] if row1 > 0 else 0
        outer_left = self.prefix_Mat[row2][col1 - 1] if col1 > 0 else 0
        common_ele = self.prefix_Mat[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0

        return last_corner - top_right - outer_left + common_ele        
