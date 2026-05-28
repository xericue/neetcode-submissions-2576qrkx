class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [0] * len(nums)
        # why do we make the first two cases?
        memo[0] = nums[0]
        memo[1] = max(memo[0], nums[1])

        # how would i actually derive that the state is the maximum
        # at any given step? is it because its the subproblem/only
        # variable i need to find at every step of the problem?
        for i in range(2, len(nums)):
            # memo[i] = max(skip, rob)
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])

        return memo[-1]