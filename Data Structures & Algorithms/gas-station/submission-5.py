class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if the cost is entirely more than the gas you get, it was doomed from the start
        # return -1
        if sum(gas) < sum(cost):
            return -1

        # keep a total cost and the result indes        
        total_cost = 0
        result_index = 0

        # iterate through the array
        for i in range(len(gas)):
            # add the difference - i.e. if youre given 1 gallon of gas and can only go 2 miles,
            # it turns negative; otherwise, you have some left overs (you can still properly
            # go through the whole array)

            # otherwise from that scenario ^, you have to update the index because we went negative
            # we dont wanna go negative; we want the index that allows us to traverse the entire
            # array with a positive difference
            total_cost += gas[i] - cost[i]
            if total_cost < 0:
                total_cost = 0
                result_index = i + 1

        return result_index