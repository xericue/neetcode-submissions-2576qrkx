class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        path = set() # add all positions in our board so we dont revisit

        def helper(i, r, c):
            # base case
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path:
                return False
            
            # recursive cases
            path.add((r, c))
            res = (helper(i + 1, r + 1, c) or 
                    helper(i + 1, r - 1, c) or 
                    helper(i + 1, r, c + 1) or 
                    helper(i + 1, r, c - 1))
            
            path.remove((r, c))
            return res
            
            # recursive case
        for j in range(rows):
            for k in range(cols):
                if helper(0, j, k):
                    print(path)
                    return True
        print(path)
        return False