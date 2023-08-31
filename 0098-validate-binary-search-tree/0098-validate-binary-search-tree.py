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
        
        def helper(self, node):
            if not node:
                return True
            
            curLeft = node.left
            if curLeft:
                while curLeft.right:
                    curLeft = curLeft.right
                
                if curLeft.val >= node.val:
                    return False
            
            curRight = node.right
            if curRight:
                while curRight.left:
                    curRight = curRight.left
                    
                if curRight.val <= node.val:
                    return False
            
            if helper(self, node.left) and helper(self, node.right):
                return True
            else:
                return False
            
        return helper(self, root)
                