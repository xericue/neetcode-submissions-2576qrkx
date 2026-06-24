class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indegrees and adj list
        adjlist = {i:[] for i in range(numCourses)}
        indeg = [0] * numCourses
        retarr = []

        for i in prerequisites:
            # a, b -> b unlocks a
            locked, key = i
            adjlist[key].append(locked)
            indeg[locked] += 1
        
        # start q
        q = collections.deque()
        for i, v in enumerate(indeg):
            if v == 0:
                q.append(i)
        
        total = 0
        while q:
            idx = q.popleft()
            retarr.append(idx)
            total += 1
            for nei in adjlist[idx]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        if total == numCourses:
            return retarr
        return []
        
            