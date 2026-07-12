class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        # we cant use a heap because its just gonna order 1 2 2 3 3 4 4 5
        # what if we sort ts
        # okay well this is a greedy problem, meaning that theres an optimal substructure - solving
        # the smallest problems optimally will lead to the global optimal solution
        
        fmap = {} # why would we use one bro

        for i in hand:
            fmap[i] = fmap.get(i, 0) + 1
        
        q = list(fmap.keys())
        heapq.heapify(q)

        # continue until ts empty
        while q:
            n = q[0] # first value Ever.
            
            # can we create this group
            for i in range(n, n + groupSize):
                if i not in fmap:
                    return False # value isnt even available
                fmap[i] -= 1
                
                # is the frequency now 0? we then pop it from our min heap
                if fmap[i] == 0:
                    # BUT, if its != the minimum value in the heap, return False immediately
                    # bc. removing it means that the next group has a hole????????????
                    if i != q[0]:
                        return False
                    heapq.heappop(q)
        return True