class Solution:
    def trap(self, height: List[int]) -> int:

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