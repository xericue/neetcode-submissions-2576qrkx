class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # what makes this a heap problem
        # at each step we wanna choose a maximum always - greedy or linear traversal
        # would take too long; instad, we can use a max heap

        prio_q = stones
        heapq.heapify_max(prio_q)

        while prio_q:
            x = heapq.heappop_max(prio_q)
            if prio_q:
                y = heapq.heappop_max(prio_q)
            else:
                return x
            
            if x > y:
                heapq.heappush_max(prio_q, x - y)

        if prio_q:
            return prio_q[0]
        return 0