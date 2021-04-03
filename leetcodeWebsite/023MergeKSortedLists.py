# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = t = ListNode()
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                t.next = l2
                l2 = l2.next
            else:
                t.next = l1
                l1 = l1.next
            t = t.next
        t.next = None
        if l1 is not None:
            t.next = l1
        else:
            t.next = l2
        return r.next

    def mergeKLists(self, lists) -> ListNode:
        if len(lists) == 0:
            return ListNode()
        r = lists[0]
        i = 1
        while i < len(lists):
            r = self.mergeTwoLists(r, lists[i])
            i += 1
        return r

def convertValueToList(lst):
    nodes = [ListNode(val=e) for e in lst]
    for i in range(1, len(nodes)):
        nodes[i-1].next = nodes[i]
    return nodes[0]
if __name__=="__main__":
    s = Solution()
    lsts = [[1, 4, 5], [1, 3, 4], [2, 6]]
    nodesLst = []

    for l in lsts:
        nodesLst.append(convertValueToList(l))
    r = s.mergeKLists(nodesLst)
    while r is not None:
        print(r.val, "->", end="")
        r = r.next

    r = s.mergeTwoLists(s.mergeTwoLists(*nodesLst[:2]),nodesLst[2])
    while r is not None:
        print(r.val, "->", end="")
        r = r.next