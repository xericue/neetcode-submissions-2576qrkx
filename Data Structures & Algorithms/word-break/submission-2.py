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

                # if the word is equal to the string that has been surely done:
                    # set current index equal to the ones above it because
                    # we're sort of going to that above and beyond to see
                    # if we previously had calculated it - since we calculated, say,
                    # dp[8] and dp[4] as both are true, dp[0] will also be true
                    # as we try to pull for "leet" == s[0:4] -> "leet"
                    # ^ so a word in the dictionary matches (out of the iterations),
                    # so we list that in our dp table

                # s[4:8] -> "code" out of "leetcode"
                if w == s[i:(i + len(w))]: 
                    dp[i] = dp[i + len(w)] # dp[7] = dp[7 + 1], for example
                    # ohhh you pull values you already calculated up top
                
                # if its true, just break out of the words dict - we dont need to do
                # more since we already found a word that works :)
                if dp[i]:
                    break
        return dp[0]
                
