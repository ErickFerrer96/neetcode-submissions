class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minVal = prices[0]
        maxProfit = 0 

        for val in prices:
            if minVal > val:
                minVal = val
            if (val-minVal) > maxProfit:
                maxProfit = val-minVal
        
        return maxProfit

            