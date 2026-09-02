class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n < 3: return max(nums)
        
        DP = [0 for _ in range(n+1)]
    
        for i in range(n): DP[i] = max(nums[i] + DP[i-2], DP[i-1])
        
        return max(DP)
