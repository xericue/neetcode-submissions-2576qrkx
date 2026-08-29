class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def dfs(num):
            print(num)
            if num in memo:
                return memo[num]
            
            new = dfs(num - 1) + dfs(num - 2)
            memo[num] = new
            return new

        return dfs(n)