# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        check = root
        while (check.val < p.val and check.val < q.val) or (check.val > p.val and check.val > q.val):
            if check.val < p.val and check.val < q.val:
                check = check.right
            else:
                check = check.left
        
        return check