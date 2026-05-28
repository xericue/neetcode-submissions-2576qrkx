class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # O(1) space
        # O(n) time
        
        # memo = [0] * len(nums)
        # you actually dont even need this because you can just set
        # prev and curr upon which to keep iterating
        # why do we make the first two cases?
        # we make the first two because their behavior is well defined
        # (the first house is the first maximum which is only itself, and
        # the second house is the maximum of the two). this also allows us
        # to keep iterating forward with proper calculations of i - 1 (the
        # amount if we skipped the third house) and i - 2 (the amount if 
        # we robbed the third house).
        prev = nums[0]
        curr = max(nums[0], nums[1])

        # how would i actually derive that the state is the maximum
        # at any given step? is it because its the subproblem/only
        # variable i need to find at every step of the problem?
        for i in range(2, len(nums)):
            prev, curr = curr, max(curr, nums[i] + prev)

        return curr