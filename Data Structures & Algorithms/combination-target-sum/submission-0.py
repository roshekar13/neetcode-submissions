class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def backtrack(curr_path):
            if sum(curr_path) == target:
                res.append(list(curr_path))
                return
            
            for num in nums:
                if curr_path and num < curr_path[-1]: continue
                curr_path.append(num)
                if sum(curr_path) <= target:
                    backtrack(curr_path)
                curr_path.pop()
            return
        
        backtrack([])

        return res
