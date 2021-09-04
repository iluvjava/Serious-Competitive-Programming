from typing import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        RowsTozero = []
        ColTozero = []
        for II in range(len(matrix)):
            for JJ in range(len(matrix[0])):
                if matrix[II][JJ] == 0: 
                    RowsTozero.append(II)
                    ColTozero.append(JJ)
        for II in RowsTozero: 
            for JJ in range(len(matrix[0])): 
                matrix[II][JJ] = 0
        for JJ in ColTozero: 
            for II in range(len(matrix)):
                matrix[II][JJ] = 0
                
        