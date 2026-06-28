class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [0] * len(points)
        
        for i, v in enumerate(points):
            x, y = v
            distances[i] = (math.sqrt((x ** 2) + (y ** 2)), [x, y])
        
        heapq.heapify(distances)
        heap = []

        ret_arr = []
        while k > 0:
                value = heapq.heappop(distances)
                ret_arr.append(value[1])
                k -= 1
                
        return ret_arr
