class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # iterate through, never adding to intervals itself
        for i in range(len(intervals)):
            # first case: newInterval is behind curr and non-overlapping
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # second case: newInterval is ahead of curr and non-overlapping
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # third case: newInterval is overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res