"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # isnt this literally just a graph traversal
        
        if not node:
            return None

        start = node

        # old to new
        otn = {}

        stk = [start]
        visited = set()
        visited.add(start)

        # CREATE ALL NODES WITH A SHADOW MAP FROM OTN
        while stk:
            # dfs
            # get the node
            curr = stk.pop()
            # create a new node out of this and map it
            otn[curr] = Node(val=curr.val) # neighbors?

            for i in curr.neighbors:
                if i not in visited:
                    visited.add(i)
                    stk.append(i)

        # NOW LOOP THROUGH IT
        # purposes: find connections, connect neighbors;
        # get the insertion point
        for old, new in otn.items():
            # for old neighbors... etc
            for i in old.neighbors:
                new_nei = otn[i]
                new.neighbors.append(new_nei)

        return otn[start]