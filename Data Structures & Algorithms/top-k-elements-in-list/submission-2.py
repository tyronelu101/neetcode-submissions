class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #loop through list
        #for each element, store in hashmap as key with count as value
        #for each hit, increase count by 1
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        
        countPairList = []

        for key, value in dic.items():
            countPairList.append((key, value))

        sortedList = sorted(countPairList, key=lambda x: x[1], reverse=True)
        
        result = []

        for i in range(k):    
            result.append(sortedList[i][0])

        return result
        
