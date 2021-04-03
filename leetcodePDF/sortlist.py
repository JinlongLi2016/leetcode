# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)
def create_link(lst):
    nodes = [ListNode(e) for e in lst]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    return nodes[0]
def output_link(link, end='None'):
    while link and link != end:
        print(link.val, end = '->')
        link = link.next
    print()
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        w = self.qs(head, None)
        
    def qs(self, st, end):
        if st == end:
            return 
        w = self.split(st, end)
        self.qs(st, w)
        self.qs(w.next, end)
        
    def split(self, st, end):
        
        if st == None:
            return None
        if st.next == end:
            return st
        if st == end:
            return None
        p = st.val
        i = st
        j = i.next
        output_link(st)
        output_link(st, end)
        
        print(i.val,  end)
        
        while j != end:
            if j.val <= p:
                i = i.next
                if i != j:
                    i.val, j.val = j.val, i.val
            j = j.next
        i.val, st.val = st.val, i.val
        return i

lk = create_link([4, 2, 1, 3])

solution = Solution()
solution.sortList(lk)