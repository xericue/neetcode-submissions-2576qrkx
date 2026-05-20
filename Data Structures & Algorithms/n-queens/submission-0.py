class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()
        neg_diag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def helper(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # recursive steps, this is when we continue
            # go through col in range(n) - every position in the current ROW
            for c in range(n):
                # skip this position if its invalid
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # otherwise, update all of our sets
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                # set it off
                helper(r + 1)
                # backtrack out of the updates
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        helper(0)
        return res
