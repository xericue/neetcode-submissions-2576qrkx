class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        dp[len(s)] = True

        # push DP - 
        for i in range(len(s) - 1, -1, -1):
            # go through all the words
            for w in wordDict:
                # if it can firstly fit
                if len(w) + i > len(s):
                    continue
                
                # now if it CAN fit, we have to process the word with its length
                # if the word equals the prefix substring
                    # set dp[len(w)] = True

                if w == s[i:(i + len(w))]: # i + length of current word
                    dp[i] = dp[i + len(w)] # dp[7] = dp[7 + 1], for example
                    # ohhh you pull values you already calculated up top
                
                if dp[i]:
                    break
        return dp[0]
                
