class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0: return 0
        best = 0
        l,r = 0,1
        while r < len(prices):
            # check for profit
            if prices[l] < prices[r]: best = max(best, prices[r]-prices[l])
            else: l = r
            r += 1
        return best