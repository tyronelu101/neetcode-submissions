class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort1 = "".join(sorted(s))
        sort2 = "".join(sorted(t))
        return sort1 == sort2