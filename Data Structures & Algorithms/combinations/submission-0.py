class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return_array = []
        cur_set = [] # initial
        nums = [i for i in range(1, n + 1)]

        # "to build each cur_set, we will need a helper method"
        # why do we need a helper function?
        def backtracking_helper(i, nums, cur_set, return_array):
            # base case: at the end of our recursion for one path we've explored, add it
            # to the return array
            if i >= len(nums):
                if len(cur_set) == k:
                    return_array.append(cur_set.copy()) # python keeps references, so append a copy
                return

            # recursive case
            # first consider the first ever case, since i is 0
            cur_set.append(nums[i])
            # recurse forward as normal but now with nums[i], NOT nums[i + 1] here
            backtracking_helper(i + 1, nums, cur_set, return_array)

            # now consider the separate path without nums[i] as we do in every subset
            cur_set.pop()
            backtracking_helper(i + 1, nums, cur_set, return_array)

        backtracking_helper(0, nums, cur_set, return_array)
        return return_array