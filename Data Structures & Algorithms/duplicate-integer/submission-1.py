class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = dict.fromkeys(nums, 0)
        for x in nums:
            numDict[x] += 1
            if(numDict[x] == 2):
                return True

        return False