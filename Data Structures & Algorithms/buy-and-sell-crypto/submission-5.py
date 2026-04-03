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
        # l = 0
        # r = 1
        # profit = 0
        # while r<len(prices):
        #     if prices[l]>prices[r]:
        #         l = r
        #         r += 1
        #     else:
        #         profit = max(profit, (prices[r] - prices[l]))
        #         r += 1
        # return profit
        import numpy as np

        current_min = np.inf
        return max([p - (current_min := min(current_min, p)) for p in prices])




