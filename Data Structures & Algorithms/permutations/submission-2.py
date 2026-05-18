class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i, perms):
            # base case
            # remember that this is from the back of the array so this is when our i is off the
            # deep end and we need to begin with our "root" of the permutations
            if i == len(nums):
                return [[]] # we're actually returning something at the end of this

            # recursive case
            curr_perms = []
            
            perms = helper(i + 1, nums)
            # loop through all the elements
            for p in perms:
                # loop through a range of the length of the permutation itself plus one (for the after)
                # where we INSERT before and after type beat
                for j in range(len(p) + 1):
                    # copy it for a new distinct version
                    p_copy = p.copy()
                    # INSERT using j before and after type beat
                    p_copy.insert(j, nums[i]) # use i to index nums
                    # append our new permutation to the list
                    curr_perms.append(p_copy)
            
            return curr_perms


            

        ret_arr = helper(0, nums)
        return ret_arr