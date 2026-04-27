class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0 
        r = n - 1

        most = 0
        while l < r:
            y = min (heights[l], heights[r])
            x = r - l
            area = y * x
            most = max(most, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return most

        