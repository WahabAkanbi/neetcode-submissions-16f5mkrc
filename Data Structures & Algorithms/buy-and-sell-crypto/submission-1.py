class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        max_profit = 0

        left = 0

        for right in range(days):
            if(prices[right] <= prices[left]):
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)

        return max_profit


        