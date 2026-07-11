class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # you can start from the back and constantly move the goal post back - if you can
        # reach element n, you can reach element n - 1, then n - i for all valid elements
        # i inductively
        n = len(nums)
        goalpost = len(nums) - 1
        
        # okay wait this Does work. its the inner logic thats stupid
        for i in range(len(nums) - 2, -1, -1):
            # if we can jump to the current goalpost (the current element is equal to or EXCEEDS
            # the needed jumps to get to the goalpost, even if its getting further away - e.g
            # [3, 0, 0, 0] - we update our goalpost to the next successful element)
            if nums[i] >= goalpost - i:
                goalpost = i
        
        # this is the idea of "greedily" tracking the next possible index you can reach
        
        return goalpost == 0