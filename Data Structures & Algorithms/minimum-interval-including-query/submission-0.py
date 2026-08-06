class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # initialization - minheap, result, intervals index, sort intervals
        intervals.sort()
        res = {}
        i = 0
        pq = []

        # main algorithm - go through sorted queries
        for q in sorted(queries):
            # add all interval lengths of intervals that contain q to the min heap
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(pq, (e - s + 1, e))
                i += 1

            # pop all invalid intervals before parsing the valid minimum interval
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            # parse the minimum interval if there are still intervals left
            if pq:
                res[q] = pq[0][0]
            else:
                res[q] = -1



        result = [res[q] for q in queries]
        return result