class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        def recurse(visited, curr_path):
            if len(curr_path) == n:
                res.append(curr_path[:])
                return
            for num in nums:
                if num not in visited:
                    # update path and seen list
                    visited.add(num)
                    curr_path.append(num)
                    # recurse
                    recurse(visited, curr_path)
                    # undo
                    curr_path.pop()
                    visited.remove(num)
        # initialize and populate res
        seen = set()
        res = []
        recurse(seen, [])
        return res