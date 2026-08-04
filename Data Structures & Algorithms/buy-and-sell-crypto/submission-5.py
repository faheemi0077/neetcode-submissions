class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            curr_profit = prices[i] - minimum
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit