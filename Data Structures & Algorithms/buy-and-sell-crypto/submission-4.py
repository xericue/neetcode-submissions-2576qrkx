class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmin = float('inf')
        profit = 0

        # look at every price
        for price in prices:
            
            # is the current price the minimum price we've already seen? if so, update it (because we always
            # want the minimum price)
            lmin = min(lmin, price)

            # update profit if necessary
            # calculation: current price minus the minimum ever seen price
            # ^ it guarantees that the minimum ever seen price is behind or equal to the current price
            # merely because we iterate through the array linearly and update if needed
            profit = max(profit, price - lmin)


        return profit