class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        global_max = -1
        while left <= right:
            global_max = max(global_max, (min(heights[right], heights[left])) * (right - left))
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                
        return global_max