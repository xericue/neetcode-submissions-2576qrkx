class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # i can use k as the size of my sliding window and then just iterate from
        # there - i thought it was two pointers at first because i saw two distinct
        # indices but this does sound much more solvable merely with a window that
        # moves left and right up through the array

        # wait no because it can be LESS than k as well
        # eh, ill just try brute force
        # remember, sliding window is essentially an application of two pointers
        
        for i, v in enumerate(nums):
            for j, d in enumerate(nums[1:]):
                if v == d and i != (j + 1) and abs(i - (j + 1)) <= k:
                    print(f"{v} == {d}; {i} and {abs(i - j)}")
                    return True
        
        return False