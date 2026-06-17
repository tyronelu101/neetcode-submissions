class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        hash_set = set(nums)
        longest_streak = 1

        for num in nums:
            current_streak = 1
            # Check if start of a sequence
            # It's the start if num-1 does not exist
            if (num - 1) not in hash_set:
                target = num + 1
                while target in hash_set:
                    target += 1
                    current_streak += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak

        return longest_streak