class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fmap = {}

        window = 0
        left = 0
        right = 0
        max_freq = 0

        while right < len(s):
            fmap[s[right]] = fmap.get(s[right], 0) + 1
            max_freq = max(max_freq, fmap[s[right]])

            while (right - left + 1) - max_freq > k:
                fmap[s[left]] -= 1
                left += 1
            
            window = max(window, right - left + 1)
            right += 1

        return window