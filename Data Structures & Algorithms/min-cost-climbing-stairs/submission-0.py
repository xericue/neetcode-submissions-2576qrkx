class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        bruh = [-1] * len(cost)

        def dp(i):
            if i >= len(cost):
                return 0

            # memoization
            if bruh[i] != -1:
                return bruh[i] # not cost[i] - thats not our solution
                # from a sub problem; thats from what we have to pull
                # to solve our sub problems

            # store the total cost at this step in array
            # wait i have to use cost[i] somewhere doe
            # so why is the recurrence relation:
            # cost[i] + min(dp(i + 1), dp(i + 2))
            # the current cost is the launch pad and then you
            # take the minimal step (whichever is better returned from the
            # recursive calls) - i.e. whether the 1 step or the 2 step was
            # better and then you cache it.

            # the caching isnt super important here; the MOST important
            # part here is the recurrence relation - understand that the
            # cost at cache[1] is gonna be the cost from cost[1] plus the
            # best possible next step.
            bruh[i] = cost[i] + min(dp(i + 1), dp(i + 2))
            return bruh[i]

        agh = min(dp(0), dp(1))
        print(bruh)
        return agh
        