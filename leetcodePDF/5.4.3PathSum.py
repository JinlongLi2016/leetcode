# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        return self.help(root, 0, sum)
    
    def help(self, root, presum, targetsum):
        if root:
            if root.left == None and root.right==None and root.val + presum == targetsum:
                return True
            return self.help(root.left, presum+ root.val, targetsum) or \
                        self.help(root.right, presum+root.val, targetsum)
        return False
    
        ## 这种方式是错的 对于叶节点的判断方式有问题(因为为空时并不能表明preSum求得的和为一个从根到叶节点的路径和)
        # if root == None and presum==targetsum:
        #     return True
        # elif root==None and presum != targetsum:
        #     return False
        # else:
        #     return self.help(root.left, presum+root.val, targetsum) or \
        #             self.help(root.right, presum+root.val, targetsum)