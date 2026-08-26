class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def process_num(n):
            n_digits = [int(d) for d in str(n)]
            res = 0
            for digit in n_digits:
                res += digit**2
            return res
        
        curr = n
        while curr != 1:
            if curr in seen: return False
            seen.add(curr)
            curr = process_num(curr)
        return True