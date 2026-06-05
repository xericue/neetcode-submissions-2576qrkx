class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return_array = []
        cur_set = [] # initial

        # "to build each cur_set, we will need a helper method"
        # why do we need a helper function?
        def backtracking_helper(i, nums, cur_set, return_array):
            # base case: at the end of our recursion for one path we've explored, add it
            # to the return array
            if i >= len(nums):
                return_array.append(cur_set.copy()) # python keeps references, so append a copy
                return
            # so backtracking isnt necessarily a feature in code; its an algorithmic way of
            # thinking about doing things - this problems necessitates distinct arrays with
            # multiple "versions" (i.e. [1, 3], [1, 2], [1], etc.) in which the most optimal
            # way would to delete each new element until theyre exhausted and then go to [1].

            # again, backtracking isnt a data structure or code - this is an actual algorithm
            # in which we consider one path and then "return up" to consider another path
            
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