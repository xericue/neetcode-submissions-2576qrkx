class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = 1

        for k in range(n): # inclusive of n
            if k + 1 <= n:
                memo[k + 1] += memo[k] # add the current step
            if k + 2 <= n:
                memo[k + 2] += memo[k] # add the current step
            
        print(memo)
        return memo[n]