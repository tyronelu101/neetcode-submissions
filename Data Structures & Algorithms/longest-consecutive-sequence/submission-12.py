class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)        
        longest_streak = 1

        for num in nums:
            current_streak = 1
            current_target = num + 1
            has_streak = False
            while True:
                for num in nums:
                    if num == current_target:
                        has_streak = True
                        break
                if has_streak:
                    current_streak += 1
                    current_target += 1
                    has_streak = False
                else:
                    break
            if current_streak > longest_streak:
                longest_streak = current_streak

        return longest_streak