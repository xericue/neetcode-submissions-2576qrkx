class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # ohhhh you can transpose (flip diagonally) and then RH (reflect horizontally)
        # transpose and reflect

        n = len(matrix)

        # transpose - this doesnt touch any of
        # the cells on the diagonal but it
        # flips it all around it

        for i in range(n):
            for j in range(i + 1, n): # skip diag.
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reflect
        for i in range(n):
            for j in range(n // 2): # youre only performing n // 2 swaps - if you 
            # hvae a 4x4 youre only swapping twice; if you hav ea 3x3 youre only swapping once
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
                # ^ stay in the same row i, but swap j and the right side (n - j - 1, -1 is for
                # index error)