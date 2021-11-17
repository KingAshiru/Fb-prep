class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = i = len(nums) - 1
        ans = [0] * len(nums)
        while i >= 0:
            if (nums[left] * nums[left]) > (nums[right] * nums[right]):
                ans[i] = nums[left] * nums[left]
                left += 1
            else:
                ans[i] = nums[right] * nums[right]
                right -= 1
            i -= 1
        
        return ans
