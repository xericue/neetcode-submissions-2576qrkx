class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn = maxx = 1
        gloMax = nums[0]

        for num in nums:
            # save the untampered curr max
            temp = num * maxx

            # calculate new currs
            maxx = max(num, minn * num, maxx * num)
            minn = min(num, minn * num, temp)
            # recalc new glo max
            gloMax = max(gloMax, maxx)

        return gloMax