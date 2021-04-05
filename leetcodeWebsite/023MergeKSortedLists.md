# Merge K sorted Lists

```python
import heapq
def merge(lists):
	heap = [(e.val, e) for e in lists]
	heapq.heapify(heap)
	
	head = ListNode()
	last = head
	while heap:
		_, node = heapq.heappop(heap)
		
		last.next = node
		last = last.next 
		
		if last.next is not None:
			heapq.heappush(heap, (last.next.val, last.next))
	return head.next
```