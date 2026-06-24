class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i : [] for i in range(numCourses)}
        indeg = [0] * numCourses

        for i in prerequisites:
            unlocked, key = i
            adjlist[key].append(unlocked)
            indeg[unlocked] += 1
        
        q = collections.deque()
        for i, v in enumerate(indeg):
            if v == 0:
                q.append(i)
    
        
        total = 0

        while q:
            key = q.popleft()
            total += 1
            for nei in adjlist[key]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        return total == numCourses
        
