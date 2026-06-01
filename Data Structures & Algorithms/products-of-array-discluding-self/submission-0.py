class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            current = 1;
            for j in range(len(nums)):
                if i != j:
                    current *= nums[j]
            result.append(current)

        return result
