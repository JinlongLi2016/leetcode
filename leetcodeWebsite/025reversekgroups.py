# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        h = ListNode(next = head)
        prev = h
        while prev is not None and prev.next is not None:
            cnt = 0
            p = prev
            while p != None and cnt < k:
                cnt += 1
                p = p.next

            if p != None:
                nxt = p.next
                p = prev.next
                nextPrev = p
				
                prev.next = nxt
				# 反转(prev, next)之间的元素
                while p != nxt:
                    q = p.next

                    p.next = prev.next
                    prev.next = p

                    p = q
                prev = nextPrev

            else:
                prev = None
        return h.next

def convertValueToList(lst):
    nodes = [ListNode(val=e) for e in lst]
    for i in range(1, len(nodes)):
        nodes[i-1].next = nodes[i]
    return nodes[0]

if __name__=="__main__":
    h = convertValueToList([1,2,3,4,5])
    s = Solution()
    t = s.reverseKGroup(h, 2)
    while t is not None:
        print(t.val, "->", end = "")
        t = t.next