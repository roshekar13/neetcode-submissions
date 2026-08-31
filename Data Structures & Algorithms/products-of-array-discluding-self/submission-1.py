class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        idx_to_excl = 0
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j != idx_to_excl:
                    prod *= nums[j]
            prod_list.append(prod)
            idx_to_excl += 1
        return prod_list
