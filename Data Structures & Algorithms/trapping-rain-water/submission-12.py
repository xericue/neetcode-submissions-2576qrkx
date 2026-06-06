class Solution:
    def trap(self, height: List[int]) -> int:
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
                # it cant be left <= right because we'll be calculating
                # the extra case such that mr is 3 but the next case after
                # the pointer cross is 0 and we'll be adding an extra 3


        return glo_max