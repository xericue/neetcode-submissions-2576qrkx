class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # modelling the choice set, n choose k
        combinations = []
        curr_comb = []

        def helper(i, curr_comb, combinations, n, k):
            # base case when its our desired outcome (the length is the correct length)
            if len(curr_comb) == k:
                combinations.append(curr_comb.copy())
                return

            # regular recursive dfs base case when i runs too far
            if i > n:
                return

            # recursive case for every integer in our set, setting off a different path
            # for each element
            for j in range(i, n + 1): # ensure we include the last element, like 5
                curr_comb.append(j)
                helper(j + 1, curr_comb, combinations, n, k)        
                curr_comb.pop()
                
        helper(1, curr_comb, combinations, n, k)
        return combinations