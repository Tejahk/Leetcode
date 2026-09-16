class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > profit:
                profit = i - min_price
        return profit 
        """
        :type prices: List[int]
        :rtype: int
        """
        