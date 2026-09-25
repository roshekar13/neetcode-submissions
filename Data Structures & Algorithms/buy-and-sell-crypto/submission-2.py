class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0: return 0
        best = 0
        l,r = 0,1
        while r < len(prices):
            if prices[r] > prices[l]:
                best = max(prices[r]-prices[l],best)
                r += 1
            else:
                l = r
                r += 1
        return best
