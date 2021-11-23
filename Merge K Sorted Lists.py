# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        cur = head = ListNode(0)
        while min_heap:
            val, i = heappop(min_heap)
            cur.next = ListNode(val)
            cur = cur.next
            
            if lists[i]:
                heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
                
        return head.next
