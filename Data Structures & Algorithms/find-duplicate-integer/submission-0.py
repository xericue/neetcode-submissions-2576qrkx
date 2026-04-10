class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f_map = {}

        for i in nums:
            if i not in f_map:
                f_map[i] = i
            else:
                return i