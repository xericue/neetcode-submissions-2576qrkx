class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # this is the duplicate to try
            count = 0
            min_count = 0
            for i in nums:
                if i == mid and count == 1:
                    return i
                elif i == mid:
                    count += 1
            
                if i <= mid:
                    min_count += 1
            
            # if min_count == len(nums[:mid]):
            if min_count <= mid:
                left = mid + 1
        
            else:
                right = mid - 1
        
        return mid
        # f_map = {}

        # for i in nums:
        #     if i not in f_map:
        #         f_map[i] = i
        #     else:
        #         return i

        # # O(n), O(n)