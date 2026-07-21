class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        at = bt = ct = False
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                at = True
            if b == target[1]:
                bt = True
            if c == target[2]:
                ct = True
        
        return at and bt and ct
        