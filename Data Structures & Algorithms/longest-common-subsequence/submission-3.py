class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}

        def longest(i, j):
            # no more string to compare
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            # good recursive scenario - they equal the same; we progress both pointers
            elif text1[i] == text2[j]:
                memo[(i, j)] = 1 + longest(i + 1, j + 1)
            
            # eh recursive scenario - we only move one, so we only care about the good one
            else:
                memo[(i, j)] = max(longest(i + 1, j), longest(i, j + 1))
            
            return memo[(i, j)]

        return longest(0, 0)