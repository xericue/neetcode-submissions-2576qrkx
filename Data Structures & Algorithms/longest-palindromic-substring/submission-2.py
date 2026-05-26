class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = [""] * len(s)
        memo[0] = s[0]

        if len(s) < 2:
            return s[:1]
        
        left = 0
        curr = memo[0]
        for i in range(1, len(s)):
            curr += s[i]
            left = 0
            while curr[left:] != ''.join(reversed(curr[left:])):
                # print(f"working with {curr}")
                # print(f"{curr[left:]} doesnt equal {''.join(reversed(curr[left:]))}")
                left += 1
            # print(f"adding {curr[left:]}")
            memo[i] = curr[left:]
        
        # left = 1
        # print(s[left:])
        # print(''.join(reversed(s[left:])))
        # print(memo)
        new_memo = sorted(memo, key = lambda string: len(string))
        return new_memo[-1]