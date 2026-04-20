class Solution:
    def trap(self, height: List[int]) -> int:

        glo_max = 0
        left = 0
        right = len(height) - 1
        ml = height[left]
        mr = height[right]
        # now that we have our two maxes, we can start to iterate through the array from
        # both sides - the maxes essentially gate us in so that we can actually
        # move each iterative left and right pointer based on whether or not we 
        # can... ???????????????

        while left < right:
            if ml < mr:
                left += 1
                # we need to recalibrate the max
                ml = max(ml, height[left])
                glo_max += ml - height[left]
            else:
                right -= 1 # doesnt matter which one we move in any case
                # we need to recalibrate our max if it is max
                mr = max(mr, height[right])
                glo_max += mr - height[right]

        return glo_max