# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def height(node):
            if node == None:
                return 0
            left = height(node.left)
            right = height(node.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        if root == None:
            return True
        
        return height(root) != -1