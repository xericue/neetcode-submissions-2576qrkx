class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        adjlist = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        visited = set()
        def dfs(curr, parent):
            # base case: invariant
            if curr in visited:
                return False
            
            # add it to visited
            visited.add(curr)

            # recurse thru neighbors
            for nei in adjlist[curr]:
                if nei == parent:
                    continue
                if not dfs(nei, curr):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n