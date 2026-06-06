class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
            m = len(grid)
            n = len(grid[0])
            # memo = [[-1] * m] * n # references?
            # memo = [[None] * n for _ in range(m)]
            memo = [[None] * n for _ in range(m)]
            memo[0][0] = grid[0][0]
            ## grid[0][2] + min(dfs(0,1), dfs(-1,2))
            ## = 1 + min(3,0)
            ## = 1 <== 
            def dfs(i, j): # 2, 1
                if i < 0 or j < 0 or i >= m or j >= n:
                    return float("inf") 
                
                if memo[i][j] is not None: # we put something here
                    return memo[i][j]
                
                rec_rel = grid[i][j] + min(dfs(i, j - 1), dfs(i - 1, j))
                memo[i][j] = rec_rel
                return rec_rel
                
            dfs(m - 1, n - 1)
            return memo[-1][-1]