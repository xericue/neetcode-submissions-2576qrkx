class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2map = {}
        s1map = {}

        if len(s1) > len(s2):
            return False

        i = 0
        j = len(s1) - 1

        for idx in s1:
            s1map[idx] = s1map.get(idx, 0) + 1
        
        for idx in range(i, j + 1):
            s2map[s2[idx]] = s2map.get(s2[idx], 0) + 1

        while j < len(s2):
            if s1map == s2map:
                return True
            
            s2map[s2[i]] -= 1
            if s2map[s2[i]] == 0:
                del s2map[s2[i]]
            i += 1

            j += 1
            if j < len(s2):
                s2map[s2[j]] = s2map.get(s2[j], 0) + 1
        
        return False