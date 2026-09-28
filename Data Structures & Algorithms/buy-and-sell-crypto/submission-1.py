class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                diff = prices[r] - prices[l]
                profit = max(profit, diff)
            r += 1
        return profit



        
        
        
        
        
        
        
        
        
        # # time O(n) space O(1)
        # l,r = 0, 1 #left = buy, right = sell
        # profit = 0

        # while r < len(prices):
        #     #check profit
        #     if prices[l] < prices[r]:
        #         p = prices[r]-prices[l]
        #         profit = max(profit, p)
        #     else:
        #         l = r
        #     r += 1
        # return profit