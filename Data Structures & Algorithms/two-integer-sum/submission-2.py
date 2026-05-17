class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for index, value in enumerate(nums):
            x = target - value
            if x in table:
                return [table[x], index]
            else:
                table[value] = index
        return []