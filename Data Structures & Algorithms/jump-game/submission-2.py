class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums) == 1: return True

        max_idx = 0
        for i,incr in enumerate(nums):
            if i > max_idx: return False
            max_idx = max(max_idx,i+incr)
            
        return True