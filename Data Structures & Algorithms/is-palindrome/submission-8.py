class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        
        i2 = len(s) - 1
        for i in range(len(s)):
            if s[i] != s[i2]:
                return False
            if i >= i2:
                break
            i2 -= 1
        return True