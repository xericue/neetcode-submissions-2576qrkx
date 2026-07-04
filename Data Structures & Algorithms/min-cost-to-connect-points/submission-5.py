class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        visited = set()
        n = len(points)
        # lets have adj define a point's distance to ALL other points 
        # inefficient but yeah

        for x, y in points:
            for nx, ny in points:
                if x == nx and y == ny:
                    continue
                adj[(x, y)].append((abs(y - ny) + abs(x - nx), (nx, ny)))
                # adj[(nx, ny)].append((abs(y - ny) + abs(x - nx), (x, y)))
        """

        for i in range(n): # 0 to like 5 for ex
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append([dist, (x2, y2)])
                adj[j].append([dist, (x1, y1)])
        """

        pq = [(0, (points[0][0], points[0][1]))] # lets just say it starts at 0 at (0, 0)]
        total_cost = 0
        while len(visited) < n:
            dist, coords = heapq.heappop(pq)
            if coords in visited:
                continue
            visited.add(coords)

            # everything else - calculating a distance to ALL other points
            # and appending all of them
            x, y = coords
            total_cost += dist

            for nei_dist, nei_coords in adj[coords]:
                if nei_coords not in visited:
                    heapq.heappush(pq, (nei_dist, nei_coords))

        return total_cost