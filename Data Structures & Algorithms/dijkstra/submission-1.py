class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # first, create an adjacency list if not already given
        adj = {} # adj lists are actually dictionaries of lists Lollll
        for i in range(n):
            adj[i] = []

        for source, dest, weight in edges:
            # for each source, link its neighbors - get every weight 
            # in the adjacency list alongside the destination
            adj[source].append([dest, weight])
        
        # okay now we have our adjacency list/we can continue
        
        distances = {}
        for i in range(n):
            distances[i] = float('inf')

        predecessors = {}
        minHeap = [(0, src)]
        distances[src] = 0

        while minHeap:
            # take the shortest path every time type stuff
            curr_dist, curr_vtx = heapq.heappop(minHeap)
            if curr_dist > distances[curr_vtx]:
                continue
            
            for neighbor, weight in adj[curr_vtx]:
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = curr_vtx
                    # push back onto the heap the new best path with the neighbor
                heapq.heappush(minHeap, (new_dist, neighbor))

        for i in range(n):
            if distances[i] == float('inf'):
                distances[i] = -1
        return distances
                