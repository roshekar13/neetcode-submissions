class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        # helper function to check if string slice [l:r] is palindromic
        def is_pal(word):
            if len(word) == 1: return True
            l,r = 0,len(word)-1
            while l<r:
                if word[l] != word[r]: return False
                l += 1
                r -= 1
            return True
        
        
        def backtrack(start,candidate):
            # max number of slices reached
            if start == n: 
                res.append(candidate[:])
                return
            
            # pick more candidate slices, use idx to mark their endpoint
            for end in range(start,n):
                curr_slice = s[start:end+1]

                # backtrack on this branch if its a palindrome
                if is_pal(curr_slice):
                    candidate.append(curr_slice)
                    backtrack(end+1,candidate)
                    # backtrack changes
                    candidate.pop()

        backtrack(0,[])
        return res
