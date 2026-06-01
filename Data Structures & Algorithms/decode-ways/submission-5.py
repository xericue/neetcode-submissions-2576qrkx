class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }
        # whats being cached is the number of times we can decode...
        # remaining strings?

        def dfs(i):
            # good base case - cache or end of string
            if i in dp:
                return dp[i]

            # invalid base case
            if s[i] == "0":
                return 0

            # now its 1-9
            res = dfs(i + 1) # number of ways we can decode
            # the remaining values - obviously at the beginning
            # its going to determine the number of ways we can
            # decode ALL values, so its sort of looking into the future
            # (and we calculate each of the future values with this
            # recursive call and below)

            # there are cases where we can check i + 2
            # if (i + 1 < len(s) and (s[i] == "1" or 
            #     (s[i] == "2" and 0 < int(s[i + 1]) < 6))): # if we do have a second character
            if (i + 1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)

            dp[i] = res
            return res

        bruh = dfs(0)
        print(bruh)
        print(dp)
        return bruh

        # memo = [""] * len(s)

        # def dp(i, curr_str):
        #     if i >= len(s):
        #         return curr_str
            
        #     if s[i] == "0":
        #         return curr_str

        #     if s[i] in memo:
        #         curr_str += s[i]
        #         return curr_str
            
        #     curr_str += dp(i + 1, curr_str) + dp(i, curr_str)

        # return dp(0, "")