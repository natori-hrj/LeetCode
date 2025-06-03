class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        if M == 0:
            return
        N = len(matrix[0])
        if N == 0:
            return

        first_row_has_zero = False
        first_col_has_zero = False

        for r in range(M):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        
        for c in range(N):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if first_row_has_zero:
            for c in range(N):
                matrix[0][c] = 0
        
        if first_col_has_zero:
            for r in range(M):
                matrix[r][0] = 0