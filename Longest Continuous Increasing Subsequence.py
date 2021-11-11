class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
                longest = max(longest, count)
            else:
                count = 1
        return longest
        
