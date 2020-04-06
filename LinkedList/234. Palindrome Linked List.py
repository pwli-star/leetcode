class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        mid = (length - 1) // 2
        pre, cur = None, head
        while mid >= 0:
            tmp = pre
            pre, cur = cur, cur.next
            pre.next = tmp
            mid -= 1
        headB = cur
        headA = pre
        if length % 2:
            headA = headA.next
        while headA:
            if headA.val != headB.val:
                return False
            headA, headB = headA.next, headB.next
        return True
