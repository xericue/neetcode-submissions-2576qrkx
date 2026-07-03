class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # so this is dijkstra's but why do we need to maintain
        # and use a visited set

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
            # if weight > dist[node]:
            #     continue
            visited.add(node) # this prevents a cycle
            t = weight # max value will be the heaviiest weight to which
            # we end up traveling
            
            # processing adjacent vertices
            for n_wei, nei in adj[node]:
                if weight + n_wei < dist[nei]:
                    # recalculate distance
                    dist[nei] = weight + n_wei
                    heapq.heappush(q, (weight + n_wei, nei))

        if len(visited) == n:
            return t
        return -1