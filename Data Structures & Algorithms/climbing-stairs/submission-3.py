class Solution:
    def climbStairs(self, n: int) -> int:
        
        bruh = [0] * (n + 1)

        bruh[0] = 1

        for i in range(n):
            if i + 1 <= n: # valid
                bruh[i + 1] += bruh[i] # why?
            if i + 2 <= n: # valid
                bruh[i + 2] += bruh[i] # why?

        return bruh[n]