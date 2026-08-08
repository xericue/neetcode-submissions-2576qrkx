class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret_arr = []
        mpq = []

        # right, lets use a heap - but do we store them by index?
        # by window? whar?
        # (nums[i], index)

        # if index is < left then GOODBYE! ADIEU!
        i = 0
        while i < len(nums):
            heapq.heappush(mpq, (-nums[i], i))
            if i >= k - 1:
                while mpq and mpq[0][1] <= i - k:
                    heapq.heappop(mpq)
                ret_arr.append(-mpq[0][0])
            i += 1
        return ret_arr