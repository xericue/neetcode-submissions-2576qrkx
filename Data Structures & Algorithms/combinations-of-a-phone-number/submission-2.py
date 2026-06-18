class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if not digits:
            return []

        curr = ""
        res = set()

        def helper(i, curr, res):
            # good base case: if i is off the deep end we know to return
            if i >= len(digits):
                res.add(curr)
                return
            
            # no guard needed i believe; this is a lot like permutations

            # recursive steps
            # for j in range(i, len(digits)):
            for char in mappings[digits[i]]:
                curr += char
                helper(i + 1, curr, res)
                curr = curr[:-1]


        helper(0, curr, res)
        new_res = []
        for i in res:
            new_res.append(i)
        return new_res