class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        if len(cost) == 1: return cost[0]
        DP = [0 for _ in range(len(cost)+1)]
        DP[0] = 0
        DP[1] = 0

        for i in range(2,len(cost)+1): DP[i] = min(DP[i-1]+cost[i-1], DP[i-2]+cost[i-2])
        return DP[len(cost)]