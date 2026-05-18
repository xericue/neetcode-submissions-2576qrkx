class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # core part of logic
        # if () you cant add ) because the curr doesnt already have two ((s
        # so default to adding ( first
        # if unclosed is False:
            # append('(')
            # continue
        res = []
        curr = ""
        instances = [0, 0] # left, right

        def helper(res, curr, instances):
            # base case: if i is off the deep end, process a copy
            if instances[0] == instances[1] == n:
                res.append(curr)
                return
            
            # recursive case:
            if instances[0] < n:
                instances[0] += 1
                helper(res, curr + "(", instances)
                instances[0] -= 1
            
            if instances[1] < instances[0]:
                instances[1] += 1
                helper(res, curr + ")", instances)
                instances[1] -= 1

        helper(res, curr, instances)
        return res