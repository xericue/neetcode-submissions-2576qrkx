class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # you can start from the back and constantly move the goal post back - if you can
        # reach element n, you can reach element n - 1, then n - i for all valid elements
        # i inductively
        n = len(nums)
        goalpost = len(nums) - 1
        
        # okay wait this Does work. its the inner logic thats stupid
        for i in range(len(nums) - 2, -1, -1):
            # can the current index reach goal?
            if nums[i] >= goalpost - i:
                goalpost = i
            
        return goalpost == 0