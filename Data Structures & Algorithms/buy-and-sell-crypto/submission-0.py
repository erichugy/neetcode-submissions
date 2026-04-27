class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0 
        n = len(prices)
        l = 0
        
        r = l + 1

        while r < n:
            most = max(most, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return most