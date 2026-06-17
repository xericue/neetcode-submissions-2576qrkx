class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        n = len(nums)

        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(idx, target):
            # if target is 0 just return true beccause you dont need to partition
            if target == 0:
                return True
            
            # base case - uhhhhhhhh if we're off the deep end
            if idx == len(nums) or target < 0:
                return False

            # okay, now if its already in memo: return it
            if memo[idx][target] != -1:
                return memo[idx][target]

            # otherwise, do the memo calculation
            memo[idx][target] = (dfs(idx + 1, target) or dfs(idx + 1, target - nums[idx]))
            # either way we skip. HOWEVER, our target changes (how much we need to
            # accumulate as the partition, being half of the array). either we skip
            # this one and dont do anything to how much we need left OR we
            # subtract the current one. whichever one leads us to zero gets us that
            # one to be True.

            return memo[idx][target]

        return dfs(0, target)