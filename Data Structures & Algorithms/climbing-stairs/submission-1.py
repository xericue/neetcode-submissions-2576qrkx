class Solution:
    def climbStairs(self, n: int) -> int:
        
        bruh = [-1] * n

        def dp(i):
            if i == n:
                return 1 # valid path/base case, count it
                # why return 1 tho?

            if i > n:
                return 0 # invalid path, dont count it

            # base state one
            if bruh[i] != -1:
                # no no no dont return 0; youre returning
                # the value thats actually cached there...
                # thats the point of memoization - not to skip over,
                # but to use information from old subproblems to
                # build toward your bigger results
                return bruh[i]
            
            bruh[i] = dp(i + 1) + dp(i + 2)
            return bruh[i]

        return dp(0)