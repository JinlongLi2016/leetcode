# Wrong Solution!

# Definition for singly-linked list.
class ListNode(object):
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
    print()

def reverselink(l):
    if not l:
        return None
    tmp = ListNode(None)
    while l:
        lNext = l.next
        l.next = tmp.next
        tmp.next = l
        
        l = lNext
    return tmp.next

def merge(l1, l2):
    p = tmp = ListNode(None)
    while l1 and l2:
        l1Next = l1.next
        l2Next = l2.next
        
        p.next = l1
        p = p.next
        p.next = l2
        p = p.next
        
        l1 = l1Next 
        l2 = l2Next
    while l1:
        p.next = l1
    while l2:
        p.next = l2
    return tmp.next

        
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        link1, link2 = ListNode(None), ListNode(None)
        p1, p2 = link1, link2
        p = head
        while p:
            p1.next = p
            p1 = p1.next
            
            p = p.next
            
            p2.next = p
            p2 = p2.next
            
            if p:
                p = p.next
        p1.next = None
        p2.next = None

        link1, link2 = link1.next, link2.next
        print('link1:');output_link(link1)

        print('link2:');output_link(link2)
        link2 = reverselink(link2)
        print('link3:'); output_link(link2)
        return merge(link1, link2)

l1 = create_link([1, 2, 3, 4])

s = Solution()
tmp = s.reorderList(l1)
output_link(tmp)
