# 103 二叉搜索树的zigzag层次遍历

Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

* mine: 层次遍历，但是将特定的行的结果进行reverse

```python
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        prev, nxt = [root], []
        finalres = []
        level = 0
        res = []
        while prev:
            t = prev.pop(0)
            if t.left:
                nxt += t.left,
            if t.right:
                nxt += t.right,
            res.append(t.val)
            if not prev:
                if level % 2:
                    res = res[::-1]
                level += 1
                finalres.append(res)
                res = []
                prev, nxt = nxt, []
        return finalres
```

