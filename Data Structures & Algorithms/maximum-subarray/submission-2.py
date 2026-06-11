class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # start sub arrays
        curr_sum = nums[0]
        max_sum = nums[0]

        # iterate through array from 2nd element
        for i in range(1, len(nums)):
            # either the current sum + current element is better or we start
            # a new array starting from the current element :p.
            curr_sum = max(nums[i], curr_sum + nums[i])

            # update max_sum
            max_sum = max(curr_sum, max_sum)

        return max_sum