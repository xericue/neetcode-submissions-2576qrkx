class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_sum = []
        ret_arr = []
        nums.sort()

        def helper(i, nums, curr_sum, ret_arr):
            # base case - if sum(curr_sum) == target
            if sum(curr_sum) == target and sorted(curr_sum) not in ret_arr:
                ret_arr.append(sorted(curr_sum).copy())
                return

            # second base case for our recursive deep end check
            # if i > len(nums) + 5:
            #     return

            # recursive case
            for j in range(i, len(nums)):
                # you actually return in here?
                if sum(curr_sum) + nums[j] > target:
                    return # oh thats faster...
                curr_sum.append(nums[j])
                helper(j, nums, curr_sum, ret_arr)
                curr_sum.pop()

        helper(0, nums, curr_sum, ret_arr)
        return ret_arr