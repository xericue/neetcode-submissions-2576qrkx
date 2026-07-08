class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        curr_sum = 0
        if len(nums) == 1:
            return nums[0]

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            total = max(curr_sum, total)
        return total