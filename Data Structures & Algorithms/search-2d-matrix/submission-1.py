import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = np.array(matrix)
        res = a.flatten()
        if target in res:
            return True
        else: 
            return False