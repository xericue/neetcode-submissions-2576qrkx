class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest order in the sorted order
        # so if we put it all in a heap, pop until k - 1, return the popped k,
        # we win

        nums = [-i for i in nums]
        heapq.heapify(nums)

        print(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -(heapq.heappop(nums))