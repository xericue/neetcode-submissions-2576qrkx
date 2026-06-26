class TimeMap:

    def __init__(self):
        self.tbkvs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tbkvs:
            self.tbkvs[key].append((timestamp, value))
        else:
            self.tbkvs[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.tbkvs:
            return res
        else:
            arr = self.tbkvs[key]

            left = 0
            right = len(arr) - 1

            # this actually requires a modified binary search - since ANY
            # value <= timestamp works, we can set a correct result here and
            # still move our left pointer. it's a bit more lenient; however,
            # it leverages that and KEEPS GOING to find a more optimal answer
            
            while left <= right: # cannot equal the same element
                mid = (left + right) // 2
                if arr[mid][0] <= timestamp:
                    res = arr[mid][1]
                    left = mid + 1                
                else:
                    right = mid - 1
            
            return res