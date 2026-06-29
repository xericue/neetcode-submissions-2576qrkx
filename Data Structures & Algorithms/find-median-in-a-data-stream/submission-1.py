class MedianFinder:

    # yeah this TLEs

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -(num))

        # we could implement a self._balance() here but let's
        # just do it in addNum().

        # _balance()
        # max is greater than min
        if (self.small and self.large and -(self.small[0]) >= self.large[0]):
            balance = -(heapq.heappop(self.small))
            heapq.heappush(self.large, balance)

        # 2nd condition: uneven size
        # wait we dont need to ask if small and large are valid here
        # Oh. its because one of them could just straight up be empty
        # but that doesnt matter; youll still balance it anyway
        if (len(self.small) > len(self.large) + 1):
            # pop from small, push to large
            balance = -(heapq.heappop(self.small))
            heapq.heappush(self.large, balance)
        
        if (len(self.small) + 1 < len(self.large)):
            # pop from large, push to small
            balance = heapq.heappop(self.large)
            heapq.heappush(self.small, -(balance))

    def findMedian(self) -> float:
        # this will be an O(1) operation
        # odd length if one of them is greater than the other
        if len(self.small) > len(self.large):
            return -(self.small[0])
        
        if len(self.small) < len(self.large):
            return self.large[0]
        
        return (-(self.small[0]) + self.large[0]) / 2