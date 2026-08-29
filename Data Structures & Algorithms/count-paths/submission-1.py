class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(0, 0): 1, (0, 1): 1, (1, 0): 1} # remove later

        def dp(i, j):
            # base case
            if i < 0 or j < 0:
                return 0

            # base case
            if (i, j) in memo:
                return memo[(i, j)]

            # recursive case - maybe two of them
            new = dp(i - 1, j) + dp(i, j - 1)
            memo[(i, j)] = new
            return new

        return dp(m - 1, n - 1)