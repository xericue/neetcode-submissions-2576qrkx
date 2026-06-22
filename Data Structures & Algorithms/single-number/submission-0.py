class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitset = 0

        for i in nums:
            bitset = bitset ^ i
        
        return bitset