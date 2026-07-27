class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # it looks like we have one pointer choosing the lowest possible integer given that its < right

        # so we wanna find left and right such that
        # - right is the greatest possible value after left
        # - left is the smallest possible value before right

        # how can we algorithmize this
        """
        maybe iterate through it with just right and then update an rmax and an lmax in the process
        this isnt necessarily a sliding window however
        """ 

        lmin = float('inf')
        profit = 0

        for price in prices:
            # look at this price. is it less than the minimum price already seen?
            lmin = min(lmin, price)

            # now what do we do with ts
            # probably calculate a profit as the problem wants us to
            profit = max(profit, price - lmin)


        return profit