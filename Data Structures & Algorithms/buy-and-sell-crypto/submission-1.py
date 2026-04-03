class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start = 0
        # end = len(prices)-1
        # maxProfit = 0
        # while start<end:
        #     maxProfit = max((prices[end]-prices[start]), maxProfit)
        #     start+=1
        #     end -= 1

        # return maxProfit
        profits = [None]*len(prices)
        for i in range(len(prices)):
            thisProfit = 0
            for j in range(i+1, len(prices)):
                thisProfit = max(thisProfit, prices[j]-prices[i])
            profits[i] = thisProfit
        return max(profits)


