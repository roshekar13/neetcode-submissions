class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [0] * (n + 1)
        if n == 0 or n == 1:
            return n
        DP[1] = 1
        DP[2] = 2
        for i in range (3,n+1):
            DP[i] = DP[i-1]+DP[i-2]
        return DP[n]