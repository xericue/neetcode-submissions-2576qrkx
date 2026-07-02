class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n + 1)}
        dist = [float('inf')] * (n + 1)
        for ui, vi, ti in times:
            adj[ui].append((ti, vi))

        visit = set()
        dist[k] = 0
        q = [(0, k)]

        t = 0
        while q:
            weight, node = heapq.heappop(q)
            if node in visit:
                continue
            visit.add(node)
            t = weight
            
            for nwei, nei in adj[node]:
                if weight + nwei < dist[nei]:
                    dist[nei] = weight + nwei
                    heapq.heappush(q, (weight + nwei, nei))

        if len(visit) == n:
            return t
        return -1