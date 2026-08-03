class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        yes = False

        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                yes = True
                break
        
        if not intervals or not yes:
            intervals.append(newInterval)
        # ^ okay so take this idea and implement it with the mega linear scans
        # i mean an inefficient way we could solve this is a bellman ford-esque manner where
        # we scan x times and each scan we merge intervals that fall in line with thiss

        left = 0
        right = 1
        while right < len(intervals):
            if intervals[left][0] <= intervals[right][0] <= intervals[left][1] <= intervals[right][1]:
                intervals[left][1] = intervals[right][1]
                intervals.pop(right)
            elif intervals[left][0] <= intervals[right][0] and intervals[left][1] >= intervals[right][1]:
                intervals.pop(right)
            else:
                left += 1
                right += 1

        return intervals