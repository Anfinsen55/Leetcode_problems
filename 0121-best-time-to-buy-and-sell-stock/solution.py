class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        total_profit =0
        while right < len(prices):
            currentprofit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                total_profit = max(currentprofit,total_profit)
            else:
                left = right
            right += 1
        return total_profit
