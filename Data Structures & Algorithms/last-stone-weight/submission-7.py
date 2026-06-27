class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # what makes this a heap problem
        # at each step we wanna choose a maximum always - greedy or linear traversal
        # would take too long; instad, we can use a max heap

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