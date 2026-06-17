class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        reverse = ""
        for i in range(len(s)-1, -1, -1):
            reverse += s[i]
        s1 = "".join(reverse.lower().split())
        s2 = "".join(s.lower().split())
    
        return  s1 == s2