class Solution:
    def climbStairs(self, n: int) -> int:
        fib = {}
        for k in range(1, n + 2): # for 1 through n inclusive
            if k <= 2:
                f = 1
            else:
                f = fib[k - 1] + fib[k - 2]
            fib[k] = f
        
        print(list(fib.keys()))
        print(fib)
        return fib[n + 1]