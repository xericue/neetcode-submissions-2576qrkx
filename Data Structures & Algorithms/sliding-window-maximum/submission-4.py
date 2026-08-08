class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret_arr = []
        mpq = []

        i = 0
        while i < len(nums):
            # push onto max heap
            heapq.heappush(mpq, (-nums[i], i))

            # if we've filled our window, start processing
            if i >= k - 1:
                
                # pop maxheap stuff thats no longer valid
                while mpq and mpq[0][1] <= i - k:
                    heapq.heappop(mpq)
                
                # append to result the 
                ret_arr.append(-mpq[0][0])
            i += 1
        return ret_arr