class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr, res = [], []
        def helper(i):
            # good base case: palindrome
                # process palindrome
            if i >= len(s): # if i is off the deep end/it made it through
                res.append(curr.copy())
                return
            
            # recursive steps for all candidates at every possible step
            for j in range(i, len(s)): # go thru from current index to rest of
            # string to generate all substrings within
                if s[i:j + 1] == (s[i:j + 1])[::-1]:
                    curr.append(s[i:j + 1])
                    helper(j + 1)
                    curr.pop()

        helper(0)
        return res

        # but the issue is that we're not tracking the REMAINING characters
        # as per some dictionary or stack(???). we'll need some way to
        # maintain every letter.
        # unless im still thinking about this wrong - i think we actually
        # need to PARTITION (make divisions) and not just append letters...
        # how?

        