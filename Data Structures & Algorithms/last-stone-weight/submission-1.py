class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []

        for stone in stones:
            heapq.heappush_max(q, stone)

        while q:
            x = heapq.heappop_max(q)
            if not q:
                return x
            y = heapq.heappop_max(q)

            if x == y:
                continue
            elif x > y:
                heapq.heappush_max(q, x - y)

        if q:
            return q[0]
        return 0