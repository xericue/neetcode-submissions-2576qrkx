class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        res_len = 0

        for i in range(len(s)):
            # odd
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    # update
                    res = s[left:right + 1]
                    res_len = (right - left + 1)
                left -= 1 # expand outward
                right += 1 # expand outward

            # even
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    # update
                    res = s[left:right + 1]
                    res_len = (right - left + 1)
                left -= 1 # expand outward
                right += 1 # expand outward
    
        return res