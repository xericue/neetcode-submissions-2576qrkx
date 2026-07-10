class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = furthest = 0
        n = len(nums)

        for i in range(n - 1):
            # new far if needed
            furthest = max(furthest, i + nums[i])
            if i == end:
                jumps += 1
                end = furthest

        return jumps