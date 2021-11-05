# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = head = ListNode(0)
        
        while l1 or l2:
            sum_ = carry
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
                
            rem = sum_ % 10
            carry = sum_ // 10
            head.next = ListNode(rem)
            head = head.next
        
        if carry:
            head.next = ListNode(carry)
        
        return dummy.next
            
        
            
        
