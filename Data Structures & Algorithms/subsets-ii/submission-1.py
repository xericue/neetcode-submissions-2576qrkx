class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        global_list = []

        # i keeps track of the height of the decision tree
        def bt(i, nums_list, bt_list):
            # base case, end of the road - append copy, return
            if i == n:
                global_list.append(bt_list.copy())
                return

            # recursive case
            bt_list.append(nums_list[i])
            bt(i + 1, nums_list, bt_list)

            while i + 1 < len(nums_list) and nums_list[i] == nums_list[i + 1]:
                i += 1
            bt_list.pop()
            bt(i + 1, nums_list, bt_list)

        bt(0, nums, [])
        return global_list