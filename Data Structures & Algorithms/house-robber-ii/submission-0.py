class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp2 = [0] * (n+1)
        if len(nums) < 3:
            return max(nums)
        
        for i in range (0,n-1):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        for j in range (1,n):
            dp2[j] = max(nums[j]+dp2[j-2],dp2[j-1])
        
        
        return max(max(dp),max(dp2))
