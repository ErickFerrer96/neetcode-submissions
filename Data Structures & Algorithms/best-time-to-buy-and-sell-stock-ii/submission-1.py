class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for idx in range(1,len(prices)):

            result = prices[idx]-prices[idx-1]
            if result >0:
                profit += result

        return profit
        