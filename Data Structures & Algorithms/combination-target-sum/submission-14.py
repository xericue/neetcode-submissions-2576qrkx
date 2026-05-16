class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_sum = []
        ret_arr = []
        nums.sort()

        def helper(i, nums, curr_sum, ret_arr):
            # base case - if sum(curr_sum) == target
            if sum(curr_sum) == target:
                ret_arr.append(curr_sum.copy())
                return
            
            # second base case if its impossible to find the combination
            if sum(curr_sum) > target:
                return

            if i >= len(nums):
                return

            # recursive case
            # for j in range(i, len(nums)):
            #     curr_sum.append(nums[j])
            #     helper(j, nums, curr_sum, ret_arr)
            #     curr_sum.pop()
            curr_sum.append(nums[i])
            helper(i, nums, curr_sum, ret_arr)
            curr_sum.pop()
            helper(i + 1, nums, curr_sum, ret_arr)

        helper(0, nums, curr_sum, ret_arr)
        return ret_arr