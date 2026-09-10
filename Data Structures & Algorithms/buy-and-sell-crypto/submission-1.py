class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(1 + i, len(prices)):
                sell = prices[j]
                res = max(sell-buy, res)
        return res
