from heapq import heappush, heappushpop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            elif num >= min_heap[0]:
                heappushpop(min_heap, num)
        
        return min_heap[0]
