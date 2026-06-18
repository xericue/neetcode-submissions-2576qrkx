class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        glo_max = 0

        # iterate thru array, maintain mono stk
        for i, height in enumerate(heights):
            start = i # maintain LAST popped element
            while stk and stk[-1][0] > height:
                tall_height, prev_idx = stk.pop()
                width = i - prev_idx
                glo_max = max(glo_max, width * tall_height)
                start = prev_idx
            stk.append((height, start))

        # clean up
        while stk:
            height, prev_idx = stk.pop()
            width = len(heights) - prev_idx
            glo_max = max(glo_max, width * height)
        return glo_max