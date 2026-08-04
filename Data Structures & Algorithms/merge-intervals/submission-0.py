class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = []

        for start, end in sorted(intervals):
            if new and start <= new[-1][1]:
                new[-1][1] = max(new[-1][1], end)
            else:
                new.append([start, end])
        
        return new