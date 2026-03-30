class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = len(prices) - 1
        while left < right:
            profit = max(profit, prices[right] - prices[left])
            left += 1
            right -= 1
        return profit