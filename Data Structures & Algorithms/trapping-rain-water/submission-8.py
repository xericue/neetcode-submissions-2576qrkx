class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # so we DO want the pointers to meet based on certain criteria
        # why do we have to keep a maxLeft and maxRight for this criteria? cant we
        # just move it based on if current[left] < current[right] and vice versa

        # because the water depends on the minimum wall, either on the left or right,
        # at any stage in the array at which water may be stored

        # so when we move the left pointer, we can calculate the amount of water
        # in that column according to the left wall because, when we move the left
        # pointer, it is guaranteed to be less than or equal to the right. thats
        # why we keep maxleft and maxright(?)

        # initialize a left and right to keep two pointers because a column's water
        # level depends on the shorter of the two walls. we use two pointers to
        # determine which one is the shorter wall to make that water level calculation
        # and then move the shorter wall inward for possibility of new calculation
        left = 0
        right = len(height) - 1
        glo_max = 0
        ml = height[left]
        mr = height[right]
        while left < right: # we dont want the left and right to equal each other
            if ml < mr: # left column is smaller
                left += 1
                # because ml is smaller, we can safely go calculate that one
                ml = max(ml, height[left])
                # ml will either be equal to the current height and be zero or 
                # be greater than curr, allowing us to calculate the water in there
                glo_max += ml - height[left]
            else:
                right -= 1
                # recalibrate the max on the right
                mr = max(mr, height[right])
                # mr will either be equal to the current height or be zero
                glo_max += mr - height[right]


        return glo_max


























"""
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
"""