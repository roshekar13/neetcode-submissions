class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Naive implementation: dictionary
        #Space-efficient: negative indexing
        for i in nums:
            idx = abs(i)-1
            if nums[idx] < 0:
                return abs(i)
            else:
                nums[idx] = -nums[idx]
        return -1 #Shouldnt trigger as long as there is a dupe