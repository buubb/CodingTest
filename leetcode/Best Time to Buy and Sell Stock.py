class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = max(prices)
        profit = 0
        for price in prices:
            min_price = min(price , min_price)
            profit = max(profit, price-min_price)
        return profit
prices = [7,1,5,3,6,4]
print(Solution.maxProfit(Solution, prices))
