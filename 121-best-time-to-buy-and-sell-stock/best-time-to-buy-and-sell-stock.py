class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp=prices[0]
        maxp=0
        for i in prices:
            minp=min(minp,i)
            profit=i-minp
            maxp=max(profit,maxp)
        return maxp
        