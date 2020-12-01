class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        columns = len(matrix[0])

        rows_idx =set()
        cols_idx = set()

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]==0:
                    rows_idx.update([i])
                    cols_idx.update([j])

        for i in range(rows):
            for j in range(columns):
                if i in rows_idx or j in cols_idx:
                    matrix[i][j]=0