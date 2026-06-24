class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O':
                return
        
            board[r][c] = "#"
            for nei in directions:
                dr, dc = r + nei[0], c + nei[1]
                dfs(dr, dc)
            
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows, cols = len(board), len(board[0])

        edge_pixels = []

        for i in range(cols): # first row, last row
            if board[0][i] == 'O':
                edge_pixels.append((0, i))
            if board[rows - 1][i] == 'O':
                edge_pixels.append((rows - 1, i))

        for i in range(1, rows - 1): # first col, last col
            if board[i][0] == 'O':
                edge_pixels.append((i, 0))
            if board[i][cols - 1]:
                edge_pixels.append((i, cols - 1))


        # 1. edge Os -> #s
        for r, c in edge_pixels:
            dfs(r, c) # no need to initialize bc its mutating

        # 2. all Os -> Xs
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # 3. all #s -> Os
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
    
