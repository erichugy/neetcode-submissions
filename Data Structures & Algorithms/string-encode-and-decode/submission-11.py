class Solution:

    def encode(self, strs: List[str]) -> str:
        breakWordChar = "-1"
        encodedChars = []
        for string in strs:
            for c in string:
                encodedChars.append(str(ord(c)))
            encodedChars.append(breakWordChar)
        return "_".join(encodedChars)
    def decode(self, s: str) -> List[str]:
        ans = []
        if not s: return []
        encodedChars = s.split("_")
        curr = []
        for encoding in encodedChars:
            if (encoding == "-1"):
                string = ''.join(curr)
                ans.append(string)
                curr = []
            else: curr.append(chr(int(encoding)))
        return ans
            
            

