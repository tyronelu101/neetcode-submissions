class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        processed = set()
        for i in range(len(strs)):
            if strs[i] in processed:
                continue
            current = [strs[i]]
            for x in range(i+1, len(strs)):
                if self.isAnagram(strs[i], strs[x]):
                    current.append(strs[x])
                    processed.add(strs[x])
            result += [current]
            current = []

        return result

    def isAnagram(self, str1, str2):
        sortedChars1 = sorted(str1)
        sortedChars2 = sorted(str2)
        return "".join(sortedChars1) == "".join(sortedChars2)
