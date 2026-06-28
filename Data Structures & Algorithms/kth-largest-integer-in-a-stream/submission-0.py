class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        heapq.heapify(self.arr)
        self.k = k
        # only keep track of the k largest elements so far - we dont need
        # the whole thing lol

        while len(self.arr) > k:
            heapq.heappop(self.arr)

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        
        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
        
        return self.arr[0]