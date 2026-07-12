class Solution(object):
    def maxProfit(self, prices):
        minPrice=prices[0]
        maxProfit=0
        for price in prices:
            if price<minPrice:
                minPrice=price
            elif price-minPrice>maxProfit:
                maxProfit=price-minPrice
        return maxProfit