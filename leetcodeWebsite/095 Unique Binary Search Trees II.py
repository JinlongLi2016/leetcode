# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def trees(nodes):
    # return a list containing all trees' roots
    if not nodes:
        return [None]
    elif len(nodes) == 1:
        return [TreeNode(val=nodes[0])]
    elif len(nodes) == 2:
        a, b = TreeNode(val=nodes[0]), TreeNode(val=nodes[1])
        a.right = b
        res = []
        res.append(a)
        a, b = TreeNode(val=nodes[0]), TreeNode(val=nodes[1])
        b.left = a
        res.append(b)
        return res

    res = []
    for idx, n in enumerate(nodes):
        ltrees = trees(nodes[:idx])
        rtrees = trees(nodes[idx+1:])
        for ltree in ltrees:
            for rtree in rtrees:
                t = TreeNode(val=n, left=ltree, right=rtree)
                res.append(t)
    return res


class Solution:
    def generateTrees(self, n: int):
        return trees(list(range(1, n + 1)))

if __name__=="__main__":
    s = Solution()
    s.generateTrees(3)