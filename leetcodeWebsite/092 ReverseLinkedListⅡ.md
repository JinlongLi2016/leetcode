# 092 Reverse Linked List Ⅱ

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.

---

* Mi

```python
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        tail = t = ListNode(next=head)
        i, p = 1, t
        lp, rp = None, None
        while i < right+1:
            if i == left:
                lp = p
            p = p.next
            i += 1
        rp = p
        p = lp.next
        lp.next = rp.next
        rp.next = None
        while p:
            pnext = p.next
            p.next = lp.next
            lp.next = p
            p = pnext
        return t.next
```



* [LetCode](https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING))

```python
class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head or m == n: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(m-1): p = p.next
        tail = p.next

        for i in range(n-m):
            tmp = p.next                  # a)
            p.next = tail.next            # b)
            tail.next = tail.next.next    # c)
            p.next.next = tmp             # d)
        return dummy.next
```



* M2: 寻找p节点的前一个节点，后面的节点以头插法插入(n - m)个，再将后面的节点拼接在最后。

寻找前一个节点，必然要引入一个dummy节点。

还需要注意corner case?
