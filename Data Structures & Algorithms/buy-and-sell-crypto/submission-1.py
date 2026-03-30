class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minbuy = prices[0]
        for i in prices:
            profit = max(profit, i - minbuy)
            minbuy = min(minbuy, i)
        return profit