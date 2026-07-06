class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures) - 1, -1, -1):
            val = temperatures[i]
            # stk is not empty and the top element is therefore
            # greater than the current element
            while stk and stk[-1][0] <= val: # mono dec.
                stk.pop()
            # append the value
            
            # check if stk is empty
            if not stk:
                arr[i] = 0
            else:
                arr[i] = stk[-1][1] - i
            stk.append((val, i))

        return arr