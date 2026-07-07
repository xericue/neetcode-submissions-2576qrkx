class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            
            # validate so as not to move fwd
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in path or board[i][j] != word[idx]:
                return False
            
            # set off path one
            path.add((i, j))
            res = (dfs(i + 1, j, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j - 1, idx + 1) or dfs(i, j + 1, idx + 1))

            # clean up
            path.remove((i, j))
            return res

        # run this on all cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
            
        return False