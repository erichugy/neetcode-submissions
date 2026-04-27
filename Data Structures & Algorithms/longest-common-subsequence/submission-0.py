class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1):
            char1 = text1[- i - 1]
            for j in range(n2):
                char2 = text2[- j - 1]
                if text1[- i - 1] == text2[- j - 1]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max([
                        dp[i][j+1],
                        dp[i+1][j]
                    ])

        return dp[-1][-1]