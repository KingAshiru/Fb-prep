class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        count = cur_sum = 0
        
        for num in nums:
            cur_sum += num
            
            if cur_sum == k:
                count += 1
            
            count += sums[cur_sum - k]
            sums[cur_sum] += 1
        
        return count
