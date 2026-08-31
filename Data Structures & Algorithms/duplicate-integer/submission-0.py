class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        done = set()
        for i in nums:
            if i not in done:
                done.add(i)
            else:
                return True
        return False