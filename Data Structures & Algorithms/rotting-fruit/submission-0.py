class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # graph bfs by screening the length of the queue every time

        # go through queue and then put all infected bananas in

        # while q
        
        minutes = -1
        fresh = 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        q = collections.deque()
        
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
            
        while q:
            # screen for length
            level = len(q)
            for _ in range(level):
                i, j = q.popleft()
                for di, dj in directions:
                    ni = di + i
                    nj = dj + j
                    
                    if ni >= 0 and nj >= 0 and ni < rows and nj < cols:
                        if grid[ni][nj] == 1:
                            # infect it
                            fresh -= 1
                            grid[ni][nj] = 2
                            q.append((ni, nj))
            minutes += 1
        
        if fresh == 0:
            return minutes
        return -1