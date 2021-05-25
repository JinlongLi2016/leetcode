# 116填充next指针

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

 

**Follow up:**

- You may only use constant extra space.
- Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

 

* M1：逐层处理向右指针，pre层的`next`指针已经被填充。`cur` 向右逐渐填充下一层。

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        pre, cur = root, None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right;
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root
```

* LC **A simple accepted solution**

```c++
public void connect(TreeLinkNode root) {
    while(root != null && root.left != null) {
        TreeLinkNode cur = root;
        while(cur != null) {
            cur.left.next = cur.right;
            cur.right.next = cur.next == null ? null : cur.next.left;
            cur = cur.next;
        }
        root = root.left;
    }
}
```

