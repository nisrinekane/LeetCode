class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#        using -1 to avoid out of range index error
        for i in range(len(matrix)-1):
#             loop inside each nested list
            for j in range(len(matrix[i])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True