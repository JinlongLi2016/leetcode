# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p = head
        q = p.next

        t = k = ListNode(next=head)
        while q:
            while q and p.val == q.val:
                q = q.next
            if p.next is q:
                k.next = p
                k = k.next
            p = q
            q = q.next
        k.next = None
        return t.next