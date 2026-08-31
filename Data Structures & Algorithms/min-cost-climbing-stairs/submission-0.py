class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        DP = [0] * (n+1)
        DP[0] = 0
        DP[1] = 0

        for i in range (2,n+1):
            DP[i] = min(cost[i-1]+DP[i-1],cost[i-2]+DP[i-2])
        return DP[n]
