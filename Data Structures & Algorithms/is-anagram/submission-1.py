class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sTable, tTable = {}, {}
        for i in range(len(s)):
            sTable[s[i]] = sTable.get(s[i], 0) + 1
            tTable[t[i]] = tTable.get(t[i], 0) + 1
    
        for c in sTable:
            if sTable[c] != tTable.get(c,0):
                return False
        return True