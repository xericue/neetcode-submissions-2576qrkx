class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            print(nums[mid])
            if nums[mid] > nums[right]:
                # so since mid doesnt actually narrow to the lesser value
                # perfectly, its not what we return;
                # mid can be the pivot at most but then left will update to
                # the value right after it. this is why we set left = mid + 1.
                left = mid + 1
            else:
                right = mid
            
        return nums[left] # escape when the
        # L == R (theyve narrowed to mid)