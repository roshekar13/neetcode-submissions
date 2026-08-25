class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_num(n):
            one_count = 0
            for i in range(10):
                one_count += n & 1
                n = n >> 1
            return one_count
        
        res = []
        for i in range(n+1):
            res.append(count_num(i))
        return res