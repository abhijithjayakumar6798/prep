class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp=prices[0]
        maxp=0
        for i in prices:
            if i<minp:
                minp=i
            else:
                maxp=max(maxp,i-minp)
        return maxp
        