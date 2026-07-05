class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1): # k stops
            prev_dist = dist.copy()
            for u, v, wei in flights:
                # if a new distance to v is better, update
                if prev_dist[u] + wei < dist[v]:
                    dist[v] = prev_dist[u] + wei
        
        if dist[dst] != float('inf'):
            return dist[dst]
        return -1