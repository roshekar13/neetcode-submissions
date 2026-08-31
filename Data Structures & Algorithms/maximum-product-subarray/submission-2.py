class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmin, cmax = 1,1

        for n in nums:
            if n == 0:
                cmin, cmax = 1,1
                continue
            temp_max = n * cmax

            cmax = max(n*cmax,n*cmin,n)
            cmin = min(temp_max,n*cmin,n)
            res = max(cmax,res)
        return res
        