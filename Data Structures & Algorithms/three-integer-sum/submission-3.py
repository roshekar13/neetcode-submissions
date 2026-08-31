class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combos = []
        n = len(nums)
        for i in range (n):
            p1 = i
            # Duplicate check
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p2 = i+1
            p3 = n-1
            while p2 < p3:
                ThreeSum = nums[p1] + nums[p2] + nums[p3]
                if ThreeSum == 0:
                    combos.append([nums[p1],nums[p2],nums[p3]])
                    p3 -= 1
                    while p2 < p3 and nums[p3] == nums[p3+1]:
                        p3 -= 1
                    while p2 < p3 and nums[p2] == nums[p2-1]:
                        p2 += 1
                    
                if ThreeSum < 0:
                    p2 += 1
                if ThreeSum > 0:
                    p3 -= 1
        return combos