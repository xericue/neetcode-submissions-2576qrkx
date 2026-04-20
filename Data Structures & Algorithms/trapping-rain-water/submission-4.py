class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        glo_max = 0
        new_new = [0] * len(height)
        for i in range(1, len(new_new) - 1):
            print(f"{max(height[i + 1:])}, {max(height[:i])}")
            new_new[i] = min(max(height[i + 1:]), max(height[:i]))
        
        print(new_new)

        for i, v in enumerate(new_new):
            if v - height[i] < 0:
                continue
            glo_max += (v - height[i])
    
        return glo_max
        # left = 0
        # right = 1
        # glo_max = 0

        # def calc_area(left, right):
        #     print(((min(height[left], height[right])) * (right - left - 1)) - sum(height[(left + 1):right]))
        #     return ((min(height[left], height[right])) * (right - left - 1)) - sum(height[(left + 1):right])

        # if len(height) == 1:
        #     return glo_max

        # while right < len(height):
        #     if height[right] >= height[left]:
        #         print(f"found an area: {left} and {right}")
        #         # this is catching the false negative at the beginning + not updating
        #         # left when it needs to; i.e. [4, 2, 1, 2] - left doesnt update to 2
        #         glo_max += calc_area(left, right)
        #         left = right
        #         right += 1
        #     else:
        #         right += 1
            
        # return glo_max
