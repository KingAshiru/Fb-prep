class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            nums[:] = nums[::-1]
            return nums
        
        inversionPoint = len(nums) - 2
        while inversionPoint >= 0 and nums[inversionPoint] >= nums[inversionPoint + 1]:
            inversionPoint -= 1
        if inversionPoint == -1:
            nums[:] = nums[::-1]
            return nums
        
        for i in reversed(range(inversionPoint + 1, len(nums))):
            if nums[i] > nums[inversionPoint]:
                nums[inversionPoint], nums[i] = nums[i], nums[inversionPoint]
                break
        
        nums[inversionPoint + 1:] = reversed(nums[inversionPoint + 1:])
        
        return nums
