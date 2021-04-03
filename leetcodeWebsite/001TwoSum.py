# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    	#　my solution
        c = 0
        r = None
        result = None
        while l1 is not None and l2 is not None:
        	c += (l1.val + l2.val)
        	node = ListNode(val=c%10)
        	if r is None:
        		r = node
        		result = r
        	else:
        		r.next = node
        		r = node
        	l1, l2 = l1.next, l2.next
        	c = c // 10
        l = l1 if l1 is not None else l2
        while l is not None:
        	c += l.val
        	node = ListNode(val=c%10)
        	r.next = node
        	r = node

        	l = l.next
        	c = c // 10
        if c != 0:
        	node = ListNode(val=c)
        	r.next = node
        return result

    def addTwoNumbers(self, l1, l2):
    	# Leet code solution
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next