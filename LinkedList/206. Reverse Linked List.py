# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        pre, curr = head, head.next
        head.next = None
        while curr:
            tmp = pre
            pre, curr = curr, curr.next
            pre.next = tmp
        return pre
            
            
        
