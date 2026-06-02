class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fmap = {}

        for i, v in enumerate(nums):
            fmap[v] = i
        
        for j, val in enumerate(nums):
            diff = target - val
            if diff in fmap and fmap[diff] != j:
                if j < fmap[diff]:
                    return [j, fmap[diff]]
                else:
                    return [fmap[diff], j]

        return []