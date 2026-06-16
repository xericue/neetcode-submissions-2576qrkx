class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # table
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]: # meaning our last index is actually better than all previous occurences Ever
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)