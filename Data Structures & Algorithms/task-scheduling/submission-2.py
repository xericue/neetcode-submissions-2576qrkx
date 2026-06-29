class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # identical tasks must be separated by n CPU cycles
        # otherwise, they can be completed sequentially
        # so, return the minimum number of CPU cycles to complete all tasks

        fmap = {}

        for i in tasks:
            fmap[i] = fmap.get(i, 0) + 1
        
        """
        i think we need to count cycles as we pop. as we do that, we can
        decrement the value in our original hash map to see if it's now
        okay to parse again?
        """
        
        cycles = 0
        maxHeap = [-freq for freq in fmap.values()]
        heapq.heapify(maxHeap)
        q = collections.deque() # [-count, next available time]

        while maxHeap or q: # one of them is nonempty - we have
        # tasks we need to process
            cycles += 1

            # process a task in the heap
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1 # because we just processed it
                if count:
                    q.append([count, cycles + n])
            
            # process a task in the queue
            if q and q[0][1] == cycles:
                new = q.popleft()
                new_count = new[0]
                heapq.heappush(maxHeap, new_count)

        
        return cycles