class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        # initializations 
        result = [-1, -1]
        res_len = float('inf')

        left = 0
        
        window = {} # dict to track what frequencies and what we have as opposed to what we need
        tmap = {}

        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        
        # have vs need - what we have in our window vs what length we need
        have = 0
        need = len(tmap) # ?

        # core logic
        for right in range(len(s)):
            # add to window, check if it was a have character
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # core comparison: if the window[char] frequency is equal to the needed frequency
            if char in tmap and window[char] == tmap[char]:
                have += 1
            
            # sliding window/left side logic
            while have == need:
                # result update
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    result = [left, right]
                
                window[s[left]] -= 1
                if s[left] in tmap and window[s[left]] < tmap[s[left]]:
                    have -= 1
                left += 1

        # extract results
        left, right = result
        if res_len == float('inf'):
            return ""
        return s[left:right + 1]