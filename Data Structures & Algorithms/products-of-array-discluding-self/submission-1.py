class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        
        #Do two passes
        #First pass we calculate the prefix and store in results
        #Second pass we calculate the postfix at each position and multiply the value 
        #with the prefix value stored in the results
        prefix = 1
        for i in range(len(nums)):
            if i-1 == -1:
                results[0] = prefix
            else:
                prefix *= nums[i-1]
                results[i] = prefix

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            print('i is and num os')
            if i+1 == len(nums):
                results[i] *= postfix
            else:
                postfix *= nums[i+1]
                results[i] *= postfix


        return results
