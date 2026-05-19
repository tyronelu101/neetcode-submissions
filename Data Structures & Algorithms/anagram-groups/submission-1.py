class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        result = []
        for i in strs:
            sortedString = "".join(sorted(i))
            if sortedString not in hashMap:
                hashMap[sortedString] = []
            hashMap[sortedString].append(i)
            
        for val in hashMap.values():
            result.append(val)
        
        return result
