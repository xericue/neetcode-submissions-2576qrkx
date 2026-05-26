class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        if len(nums) < 3:
            return max(nums[0], nums[1])
        memo = [0] * (len(nums) - 1)
        memo[0] = nums[0] # maybe max btw. nums[0] and nums[-1]?
        memo[1] = max(memo[0], nums[1])

        for i in range(2, len(nums) - 1):
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])

        memo_two = [0] * (len(nums) - 1)
        memo_two[0] = nums[1] # maybe max btw. nums[0] and nums[-1]?
        memo_two[1] = max(memo_two[0], nums[2])

        for i in range(2, len(nums) - 1):
            memo_two[i] = max(memo_two[i - 1], nums[i + 1] + memo_two[i - 2])

        return max(memo[-1], memo_two[-1])