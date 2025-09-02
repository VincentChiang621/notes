class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res = 0, 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            res = max(profit, res)

            # found a lower `dip` for us to buy in
            if prices[r] < prices[l]:
                l = r

        return res