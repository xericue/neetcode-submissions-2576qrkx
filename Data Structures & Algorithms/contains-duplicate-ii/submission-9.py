class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window
        # a set tests membership - check if the value is already in our window

        # so i think the main idea is that we dont actually need to keep track of stuff
        # like crazy; its literally just if two elements are in our window. it doesnt
        # matter if i - j <= k or i - j < k because our window size immediately
        # accommodates for all elements in there anyway.

        window = set()
        left = 0

        for right in range(len(nums)):
            if right + left > k: # if the window size is 2 big
            # wait, why does right + left not work? isnt it 0 + 3 <= k
            # bro right and left start at the same value its always gonna start as 0 < 3.
            # therefore you need to check if your window size is too big
            # if 0 + 0 > k (no) so continue; otherwise, remove from the window and inc. left
                window.remove(nums[left])
                left += 1
            # if the current element is in the window, return true
            if nums[right] in window:
                return True
            # else, add to the window as normal
            window.add(nums[right])

        # otherwise all, return false
        return False