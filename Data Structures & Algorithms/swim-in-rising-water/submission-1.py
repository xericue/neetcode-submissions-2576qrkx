class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra's in which we search for the path with the smallest max height
        n = len(grid)
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        # (max height seen, (r, c))
        pq = [(grid[0][0], (0, 0))]
        visited.add((0, 0))

        path = []
        time = 0

        # bfs solution
        while pq:
            max_height, coords = heapq.heappop(pq)
            if coords == (n - 1, n - 1):
                return max_height

            for dr, dc in directions:
                # consult all directions
                nr, nc = dr + coords[0], dc + coords[1]
                if nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                # max height is either the neighbor or the current height
                heapq.heappush(pq, (max(grid[nr][nc], max_height), (nr, nc)))