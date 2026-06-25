class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        total = 0
        adj = {i:[] for i in range(n)}

        for i in edges:
            n1, n2 = i
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
            
        for node in adj:
            if node not in visited:
                total += 1
                dfs(node)
        
        return total