class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        new = sorted(self.arr)
        if len(new) % 2 == 0:
            left = 0
            right = len(new)
            return (new[(left + right) // 2] + new[((left + right) // 2) - 1]) / 2
        
        else:
            left = 0
            right = len(new)
            return new[(left + right) // 2]
        