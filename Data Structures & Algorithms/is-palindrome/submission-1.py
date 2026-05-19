class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = "".join(x.lower() for x in s if x.isalnum())
        return cleanString == cleanString[::-1]
