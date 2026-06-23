class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dis question disgusting 😂
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        # initialize two queues, one for each border
        pq = collections.deque()
        aq = collections.deque()

        # you also need a set of seen positions so taht
        # you dont repetitively add elements
        pset = set()
        aset = set()

        rows, cols = len(heights), len(heights[0])


        # before we run bfs, we clearly have to add all edges
        # of each respective ocean into the queues!
        for j in range(cols): # top row
            pq.append((0, j))
            pset.add((0, j))

        for j in range(1, rows): # left wall
            pq.append((j, 0))
            pset.add((j, 0))

        for k in range(rows): # far right wall
            aq.append((k, cols - 1))
            aset.add((k, cols - 1))
            
        for k in range(cols - 1): # bottom row excluding last
            aq.append((rows - 1, k))
            aset.add((rows - 1, k))

        # run two bfs' - youd therefore benefit from a fn()
        def bfs(q, seen):
            # erm XD
            # go thru q
            while q:
                r, c = q.popleft()
                # its on the q BECAUSE we can reach it!

                for nei in directions:
                    dr, dc = r + nei[0], c + nei[1]
                    # if valid
                    # WHAT CELLS CAN FLOW WATER TO **US**
                    # are our neighbors >= curr ([r][c])? if so,
                    # water can flow from that neighbor to this
                    # current cell
                    if dc >= 0 and dc < cols and dr >= 0 and dr < rows and heights[dr][dc] >= heights[r][c] and (dr, dc) not in seen:
                        # we have a new position
                        seen.add((dr, dc))
                        q.append((dr, dc))
    
        pc = bfs(pq, pset)
        ac = bfs(aq, aset)

        # now, return their intersection
        return list(pset.intersection(aset))

        # the essence of this algorithm is that we get all
        # cells whose water can flow into each respective
        # ocean and then compute their intersection

