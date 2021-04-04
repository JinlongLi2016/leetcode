# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_link(lst):
    nodes = [ListNode(e) for e in lst]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    return nodes[0]
def output_link(link):
    while link:
        print(link.val, end = '->')
        link = link.next
# the same as split in squick sort()

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        st = p = ListNode(x)
        p.next = head
        q = head
        qprev = p

        while q:
            if q.val < x:
                # p = p.next
                if p != qprev:
                    qprev.next = q.next
                    q.next = p.next
                    p.next = q

                    p = p.next

                    q = qprev.next
                else:
                    p = p.next
                    q = q.next
                    qprev = qprev.next
            else:
                q = q.next
                qprev = qprev.next

        return st.next

s = Solution()
partlink = s.partition(create_link([1, 4, 3, 2, 5, 2]), 3)

output_link(partlink)