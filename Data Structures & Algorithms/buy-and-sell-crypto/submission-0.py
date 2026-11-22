class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value=float('inf')
        profit = 0

        for i, p in enumerate(prices):
            profit = max(profit,  (p - min_value))

            min_value = min(min_value, p)
        
        return profit



        