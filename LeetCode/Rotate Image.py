class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            matrix[i] = matrix[i] * 2

        for i in range(n):
            for j in range(n):
                matrix[j][(2*n)-1-i] = matrix[i][j]

        for i in range(n):
            matrix[i] = matrix[i][n:]
        