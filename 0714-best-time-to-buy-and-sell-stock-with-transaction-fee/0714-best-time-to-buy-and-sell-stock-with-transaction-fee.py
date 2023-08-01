class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sold = 0
        taken = -math.inf

        for price in prices:
          sold = max(sold, taken + price)
          taken = max(taken, sold - price - fee)

        return sold