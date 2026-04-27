class Solution:
    offset = 10
    def encode(self, strs: List[str]) -> str:
        ans = ""

        for string in strs:
            newString = ""
            for char in string:
                newString += chr(ord(char) + Solution.offset)
            ans+= newString + " "
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        newString = ""
        for char in s:
            if char == " ":
                ans.append(newString)
                newString = ""
            else:
                newString += chr(ord(char) - Solution.offset)
        return ans
        