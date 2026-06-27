class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # turning all operations negative makes a min heap a max heap because
        # each value thats more "minimal" will actually be more maximal once
        # reversed. -7 < -3, but then reversed is 7 > 3
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while stones:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
            else:
                return -x
            
            if x < y:
                heapq.heappush(stones, -(y - x))

        if stones:
            return -(stones[0])
        return 0