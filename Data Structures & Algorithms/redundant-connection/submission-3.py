class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        print(parent)
        # def stuff

        def find(x):
            # recursive search until representative
            if parent[x] != x:
                return find(parent[x])
            else:
                return x
        
        def union(x, y):
            # union by representatives
            n1 = find(y)
            n2 = find(x)
            if n1 == n2:
                return False
            parent[n1] = n2
            return True

        # eerrrrmmmm?
        # go through every edge


        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]