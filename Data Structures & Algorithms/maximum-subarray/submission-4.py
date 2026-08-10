class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        curr,res = 0,nums[0]

        for n in nums:
            curr += n
            res = max(res,curr)
            if curr < 0: curr = 0
        
        return res