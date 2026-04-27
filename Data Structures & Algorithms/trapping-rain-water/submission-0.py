class Solution:
    def trap(self, height: List[int]) -> int:
        """Solution
        We can store the prefix maximum in an array by iterating from left to right 
        and the suffix maximum in another array by iterating from right to left. 
        Once these arrays are built, we can iterate through the array with index i 
        and calculate the total water trapped at each position using the formula: 
        min(prefix[i], suffix[i]) - height[i]

        Runtime: o(n) - 3 pass
        Space: o(n) - 3 extra arrays of length n

        """
        # n = len(height)
        # prefixRain = [0] * n
        # suffixRain = [0] * n 
            
        # prefixMax = 0
        # suffixMax = 0
        # for i in range(n):
        #     if height[i] >= prefixMax:
        #         prefixMax = height[i]
        #     else:
        #         prefixRain[i] = prefixMax - height[i]

        #     i = i + 1
        #     if height[-i] >= suffixMax:
        #         suffixMax = height[-i]
        #     else:
        #         suffixRain[-i] = suffixMax - height[-i]
        
        # total = 0

        # for i in range(n):
        #     total += min(prefixRain[i], suffixRain[i])
        
        # return total

        """Optimal Solution - two pointers
        Runtime: o(n) - 1 pass
        Space: o(1)

        Trick: 
        If we move the left pointer before the right if the leftMax < rightMax, 
        then leftMax is the threshold of how much water that could be contained at height[i],
        SO we don't actually need to know what the rightMax value is, or even what it could eventually be, if leftMax is smaller
        """
        n = len(height)
        total = 0
        leftMax = height[0]
        rightMax = height[n-1]
        l, r = 0, n - 1

        while l < r:
            if leftMax < rightMax:
                l += 1
                if leftMax < height[l]:
                    leftMax = height[l]
                else:
                    total += leftMax - height[l]
            else:
                r -= 1
                if rightMax < height[r]:
                    rightMax = height[r]
                else:
                    total += rightMax - height[r]
        
        return total
                