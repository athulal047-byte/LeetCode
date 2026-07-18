class Solution(object):
    def maxProfit(self, prices):
        
        minprice=prices[0]
        maxprice=0
        for i in range(len(prices)):
            if minprice >= prices[i]:
                minprice=prices[i]
            else:
                profit=prices[i]-minprice
                if maxprice<profit:
                    maxprice=profit
        return maxprice