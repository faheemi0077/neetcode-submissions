class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit = 0
        while right < len(prices):
            difference = prices[right] - prices[left]
            if difference >= 0:
                maxprofit = max(difference, maxprofit)
            else:
                left = right
            right += 1
        return maxprofit
