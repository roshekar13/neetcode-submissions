class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        if len(nums) < 3:
            return max(nums)
        
        for i in range (n):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        
        return max(dp)
