class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        
        for from_i, to_i in tickets:
            heapq.heappush(adj[from_i], to_i)
        
        path = []

        # while q:
        #     curr = q.pop()
            
        #     path.append(curr)
        #     if adj[curr]:
        #         weight, nei = heapq.heappop(adj[curr])
        #         q.append(nei)
        def dfs(src):
            while adj[src]:
                dst = heapq.heappop(adj[src])
                dfs(dst)
            path.append(src)
        
        dfs('JFK')
        return path[::-1]