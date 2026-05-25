class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        uniq_combs = []
        curr_comb = []
        candidates.sort() # in memory

        def helper(i, curr_comb, uniq_combs):
            # base case - criteria satisfaction
            if sum(curr_comb) == target:
                uniq_combs.append(curr_comb.copy()) # pass a copy
                return

            # base case - off the deep end
            if sum(curr_comb) > target or i == len(candidates):
                return

            # recursive case # range 0 to 5 (0, 1, 2, 3, 4):
            # curr_comb = [1], helper recurses with i = 1
            # range 1 to 5 (1, 2, 3, 4):
            # curr_comb = [1, 2] 
            curr_comb.append(candidates[i])
            helper(i + 1, curr_comb, uniq_combs)
            
            curr_comb.pop()

            # while loop here so as not to set off paths of duplicates as we iterate
            # regular throughout our array
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, curr_comb, uniq_combs)

        helper(0, curr_comb, uniq_combs)

        return uniq_combs