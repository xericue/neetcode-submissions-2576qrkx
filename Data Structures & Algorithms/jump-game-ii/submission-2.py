class Solution:
    def jump(self, nums: List[int]) -> int:
        # every time you take a jump, increment a count by one
        n = len(nums)

        best = 0 # increment it based on the regions youve hit
        end = far = 0

        for i in range(n - 1): # dont hit the last region
            # we need to keep a marker for the end of our current region and a marker
            # for the furthest node we can touch
            far = max(far, nums[i] + i)
            if i == end:
                best += 1
                end = far

        return best