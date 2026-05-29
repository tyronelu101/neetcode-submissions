class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            #Find the delimiter
            #The length is just i until the delimiter
            #index of delimiter+1 is the first character of the word.
            #Repeat
            delimIndex = 0
            j = i
            while(j < len(s)):
                if(s[j] == "#"):
                    delimIndex = j
                    break
                j+=1
            
            # 5#hello5#worldOutput limit exceeded
            length = int(s[i:delimIndex])
            result.append(s[delimIndex+1:delimIndex + 1 + length])
            i = delimIndex + 1 + length
           
        return result