class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1: return 0

        l,r = 0,0
        res = 0

        while r < len(nums)-1:
            local_max = 0
            
            for i in range(l,r+1): local_max = max(local_max, i+nums[i])
            
            l = r+1
            r = local_max
            res += 1
            
        return res
            
