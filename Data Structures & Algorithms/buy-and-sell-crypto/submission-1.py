class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0 
        n = len(prices)
        l = 0
        
        r = l + 1

        while r < n:
            if prices[r] < prices[l]:
                l = r
            else:
                most = max(most, prices[r] - prices[l])
            r += 1
        
        return most