class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for curr_digit in nums:
            for item in res[:]:
                res.append( item + [curr_digit])
        return res