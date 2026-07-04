class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        visited = set()
        n = len(points)
        # lets have adj define a point's distance to ALL other points 

        for x, y in points:
            for nx, ny in points:
                if x == nx and y == ny:
                    continue
                adj[(x, y)].append((abs(y - ny) + abs(x - nx), (nx, ny)))

        pq = [(0, (points[0][0], points[0][1]))] # start @ a well defined start

        total_cost = 0
        while len(visited) < n:
            dist, coords = heapq.heappop(pq)
            if coords in visited:
                continue
            visited.add(coords)

            # everything else - calculating a distance to ALL other points
            x, y = coords
            total_cost += dist

            for nei_dist, nei_coords in adj[coords]:
                if nei_coords not in visited:
                    heapq.heappush(pq, (nei_dist, nei_coords))

        return total_cost