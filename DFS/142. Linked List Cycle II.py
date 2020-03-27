# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 先用快慢指针确定有无环，若有环，先确定首次相遇的位置；然后将快指针指向头结点，慢指针不动，如果快慢指针相遇，直接返回，否则每个指针各走一步，直到相遇
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        fast, slow = head, head
        step = 0
        while fast:
            try:
                step += 1
                fast, slow = fast.next.next, slow.next
                if fast == slow:
                    fast = head
                    while fast != slow:
                        fast = fast.next
                        slow = slow.next
                    return fast
            except Exception:
                return None
        
