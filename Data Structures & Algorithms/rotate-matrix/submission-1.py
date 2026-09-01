class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # operation 1: transpose along main diagonal
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # operation 2: reflection along y axis
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        #return matrix


