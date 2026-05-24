class Solution:
    def climbStairs(self, n: int) -> int:
        
        bruh = [0] * (n + 1)

        # it takes one step to get to our very first case
        bruh[0] = 1

        for i in range(n):
            # if one step up is a valid case, we're going to
            # memoize that we've done it by setting that step
            # to 
            if i + 1 <= n: # valid
                bruh[i + 1] += bruh[i] # why?
            if i + 2 <= n: # valid
                bruh[i + 2] += bruh[i] # why?

        return bruh[n]