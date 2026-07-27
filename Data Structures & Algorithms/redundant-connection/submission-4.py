class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            # recursive search until representative
            if parent[x] != x:
                return find(parent[x])
            else:
                return x
        
        def union(x, y):
            # union by representatives
            n1 = find(x)
            n2 = find(y)
            if n1 == n2:
                return False
            parent[n1] = n2
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]