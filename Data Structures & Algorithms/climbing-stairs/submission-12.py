class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def dp(num):
            if num in memo:
                return memo[num]
            
            new = dp(num - 1) + dp(num - 2)
            memo[num] = new

            return new
        
        return dp(n)