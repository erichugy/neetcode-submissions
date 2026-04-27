class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        for i in range(n):
            prefix[i] = max(prefix[i-1] if i > 0 else 0, height[i])
            suffix[n - i - 1] = max(suffix[n - i] if i > 0 else 0 , height[n - i - 1])

        print(prefix)
        print(suffix)

        for i in range(n):
            maxH = min(prefix[i], suffix[i])
            total += max(maxH - height[i], 0)

                
        return total
