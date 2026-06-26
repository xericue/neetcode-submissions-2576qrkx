class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
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
                return 0
                # if you try to union
                # the same node That Is
                # Wrong. they may have the
                # same parent so we didnt
                # actually union these

            parent[n1] = n2
            return 1

        # eerrrrmmmm?
        # go through every edge

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2) # should
            # be 1 or 0... ermmm

        return res