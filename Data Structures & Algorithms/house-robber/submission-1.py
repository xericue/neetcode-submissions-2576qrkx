class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        memo = [0] * len(nums)
        memo[0] = nums[0]
        memo[1] = max (memo[0], nums[1])
        
        for house in range(2, len(nums)):
            memo[house] = max(memo[house - 1], nums[house] + memo[house - 2])
        
        return memo[-1]