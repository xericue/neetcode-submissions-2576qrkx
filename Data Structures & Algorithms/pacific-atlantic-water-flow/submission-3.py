class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # so we need to define a dfs FUNCTION because we're gonna be doing two separate ones
        pacific_queue = []
        atlantic_queue = []

        pset = set()
        aset = set()

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        venn_diagram = []

        rows = len(heights)
        cols = len(heights[0])

        # okay wait im actually really close
        for r in range(rows):
            pacific_queue.append((r, 0))
            pset.add((r, 0)) # why the hell are we adding them all to visited?
            # i guess it doesnt make sense to go backwards/sideways to your other edge pieces
            atlantic_queue.append((r, cols - 1))
            aset.add((r, cols - 1))

        for c in range(1, cols):
            # pacific - top row
            pacific_queue.append((0, c))
            pset.add((0, c))

        for c in range(cols - 1):
            # atlantic - bottom row
            atlantic_queue.append((rows - 1, c))
            aset.add((rows - 1, c))

        
        def dfs(stk, seen):
            
            while stk:
                r, c = stk.pop()

                seen.add((r, c)) # this is the only value of the dfs
                
                # go thru neighbors
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    # v im already checking if its not in seen HERE?
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                        # there needs to be some sort of processing here?
                        stk.append((nr, nc))


        dfs(atlantic_queue, aset)
        dfs(pacific_queue, pset)

        for cell in aset:
            if cell in pset:
                venn_diagram.append(cell)

        return venn_diagram