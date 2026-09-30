class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        global_list = []

        def bt(i, nums_list, bt_list):
            # base case
            if i >= len(nums):
                global_list.append(bt_list.copy())
                return

            # recursive case
            bt_list.append(nums_list[i])
            bt(i + 1, nums_list, bt_list)
            # backtrack by popping
            bt_list.pop()
            bt(i + 1, nums_list, bt_list)
        
        bt(0, nums, [])

        return global_list