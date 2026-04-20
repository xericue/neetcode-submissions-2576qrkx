class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # well yeah, we keep a dictionary to check against
        fmap = {}

        for i in nums:
            if i in fmap:
                return True
            fmap[i] = 1
        return False