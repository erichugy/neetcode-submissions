class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        most = 0
        for n in nums:
            if n-1 not in unique:
                count = 1
                while n + count in unique:
                    count = count + 1
                most = max(most, count)

        return most