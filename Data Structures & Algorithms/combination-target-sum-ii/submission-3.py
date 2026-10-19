import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        if not candidates: return []
        n = len(candidates)
        def backtrack(idx): # track current idx to avoid dupsed
            if sum(curr) == target: res.append(copy.deepcopy(curr))
            for i in range(idx,n):
                # skip dupes at same recursion level
                if i > idx and candidates[i] == candidates[i-1]: continue
                num = candidates[i]
                if sum(curr)+num <= target:
                    curr.append(num)
                    #print(idx,curr)
                    backtrack(i+1)
                    curr.pop() # undo action
                
        
        curr = []
        backtrack(0)
        return res
