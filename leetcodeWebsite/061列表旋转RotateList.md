
*  My Solution: 7mins, 误了n=0的情况

找到倒数(k+1)th节点，也就是倒数kth节点的前一个节点，然后进行列表剪切

```python
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
            
        if n == 0:
            return head
        
        k = k % n 
        
        p = q = head
        i = 1
        while i <= k:
            q = q.next
            i += 1
        while q.next is not None:
            q = q.next
            p = p.next
        q.next = head
        
        head = p.next
        p.next = None
        
        return head
```









* Others

通过循环链表来做？[link](https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer
```

```python

```


