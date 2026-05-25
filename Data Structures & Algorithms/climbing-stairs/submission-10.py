class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)

        for k in range(n + 1): # inclusive of n
            if k + 1 <= 2: # because its zero indexed
                memo[k] = 1
            if k + 1 <= n:
                memo[k + 1] += memo[k] # add the current step
            if k + 2 <= n:
                memo[k + 2] += memo[k] # add the current step
            
        print(memo)
        return memo[n]