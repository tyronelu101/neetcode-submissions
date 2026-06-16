class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)        
        longest_streak = 1

        for num in nums:
            current_streak = 1
            next = num + 1
            while True:
                hit = False
                for num in nums:
                    if num == next:
                        hit = True
                        break
                if hit:
                    current_streak += 1
                    next += 1
                else :
                    break
            if current_streak > longest_streak:
                longest_streak = current_streak
                            
        return longest_streak