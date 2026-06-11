class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goalpost = len(nums) - 1

        # work backwards to move goalpost backwards
        # dont use goalpost in the range bc we're actually changing it
        for i in range (len(nums) - 1, -1, -1):
            if i + nums[i] >= goalpost: # goal - 1
                goalpost = i

        return goalpost == 0
            
