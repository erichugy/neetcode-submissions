class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m: return False

        counts = [0] * 26

        for i in range(n):
            counts[ord(s[i])-ord('a') ] += 1
            counts[ord(t[i])-ord('a') ] -= 1

        return not any(counts)

