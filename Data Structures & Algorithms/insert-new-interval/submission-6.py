class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        # [1, 3], [2, 5], [4, 6]

        # what if we insert it first then deal with the consequences later
        # hm it has to be sorted in ascending order though
        # Yo What If We Just Sort() It Lol And Then Do Better

        # this feels like a two pointers problem where i have Oneeee and then Twooo and then Maybe Threeeeee
        # [1, 3], [2, 5], [4, 6]
        # 1 < 2 < 3 < 5 -> [1, 5]
        # 1 < 4 < 5 < 6 -> [1, 6]

        # ^ okay so take this idea and implement it with the mega linear scans
        # i mean an inefficient way we could solve this is a bellman ford-esque manner where
        # we scan x times and each scan we merge intervals that fall in line with thiss

        for _ in range(len(intervals)):
            left = 0
            right = 1
            while right < len(intervals):
                if intervals[left][0] <= intervals[right][0] <= intervals[left][1] <= intervals[right][1]:
                    intervals[left][1] = intervals[right][1]
                    intervals.pop(right)
                elif intervals[left][0] <= intervals[right][0] and intervals[left][1] >= intervals[right][1]:
                    intervals.pop(right)
                                    
                left += 1
                right += 1

        print(intervals)
        return intervals