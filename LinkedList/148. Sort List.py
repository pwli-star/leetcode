# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        mid, slow, fast = None, head, head
        while fast and fast.next:
            mid, slow, fast = slow, slow.next, fast.next.next
        # trim to 2 lists
        mid.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)
        
    def merge(self, l1, l2):
        # print(l1, l2)
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
