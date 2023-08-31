# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
       
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack[-1]
            stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        
        return True
        