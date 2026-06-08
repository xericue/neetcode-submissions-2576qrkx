class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 # last index 

        global_left = height[left]
        global_right = height[right]

        area = 0

        while left < right:
            if global_left < global_right:
                # logic for handling left wall's max
                # move left up to calculate a new max if possible
                left += 1

                # compare the new height with the old max
                # if its greater, then no area will be added
                # if its less than, area will be added
                global_left = max(global_left, height[left])
                area += global_left - height[left]
            else:
                # logic for handling right wall's max
                right -= 1
                global_right = max(global_right, height[right])
                area += global_right - height[right]
        return area
        