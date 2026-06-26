class TimeMap:

    def __init__(self):
        self.tbkvs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tbkvs:
            self.tbkvs[key].append((timestamp, value))
        else:
            self.tbkvs[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tbkvs:
            return ""
        else:
            # ohhh i think this is where we would do the binary search? No?
            """
            key is in tbkvs 
            now we try to find its timestamp by just indexing
            if its there, great - return it
            otherwise, return a value with a tbkvs timestamp <= timestamp

            if there are multiple of these (1 2 3 | 4 | and you look at 1 2 3),
            return 3 (the biggest tbkvs timestamp)
            
            for a working demo, lets just assume it exists
            """
            # found it; this gives me the list. i need to run a binary search on
            # the arr by the timestamps
            arr = self.tbkvs[key]

            left = 0
            right = len(arr) - 1
            mid = 0

            res = ""

            while left <= right: # cannot equal the same element
                mid = (left + right) // 2
                if arr[mid][0] <= timestamp:
                    res = arr[mid][1]
                    left = mid + 1                
                else:
                    right = mid - 1
            
            return res