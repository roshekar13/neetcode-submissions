class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)-1):
            if max(prices[i+1:]) - prices[i] > best:
                best = max(prices[i+1:]) - prices[i]
        return best