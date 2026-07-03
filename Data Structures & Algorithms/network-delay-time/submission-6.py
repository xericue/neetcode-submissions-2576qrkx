class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        visited = set()
        # create adj list
        adj = {i : [] for i in range(1, n + 1)}
        # path not needed

        for ui, vi, ti in times:
            adj[ui].append((ti, vi))

        q = [(0, k)]

        t = 0 # this is to store the latest time because the latest time
        # will indicate how long it took to get the absolute longest path connected
        # in the entire graph
        while q:
            weight, node = heapq.heappop(q)

            if node in visited:
                continue
            visited.add(node) # this prevents a cycle
            t = max(t, weight)
            # this is because dijkstra's calculates the shortest path from an
            # insertion point - so its not really the heaviest weight that's
            # processed last but the longest path which aggregates throughout
            # the whole algorithm
            
            # processing adjacent vertices
            for n_wei, nei in adj[node]:
                if weight + n_wei < dist[nei]:
                    # recalculate distance
                    dist[nei] = weight + n_wei
                    heapq.heappush(q, (weight + n_wei, nei))

        if len(visited) == n:
            return t
        return -1