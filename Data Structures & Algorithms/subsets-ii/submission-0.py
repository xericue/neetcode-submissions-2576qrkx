class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # so first we sort our array so that we can implement our skip condition
        nums.sort()

        # and then we define our return array and initialize a current set
        ret_arr = []
        curr_set = []

        # then we define a helper function to consider every possible path starting from a root
        def bt(i, nums, ret_arr, curr_set):
            # base case
            # tip for base cases: think of where i in an iterative solution would end first
            # i.e. look at your array/problem and go "okay, where does i/our iterator stop"
            # -> when i falls off the deep end (is at the end of the array), so do that!
            if i >= len(nums):
                # this is where we then append a copy (not a reference) to our ret_arr
                ret_arr.append(curr_set.copy())
                return
            
            # recursive cases
            # 1. path with nums[i] INCLUDING the repeated values
            curr_set.append(nums[i])
            bt(i + 1, nums, ret_arr, curr_set) # send this path off on its own, self-guided recursion
            
            # 2. path without nums[i] NOR ANY repeated values
            # loop to ensure we skip all neighbors
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            curr_set.pop()
            bt(i + 1, nums, ret_arr, curr_set) # send this path off on its own, self-guided recursion
            


        bt(0, nums, ret_arr, curr_set)
        return ret_arr