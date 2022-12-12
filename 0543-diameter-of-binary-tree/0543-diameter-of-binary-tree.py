# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    diam = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def height(rootNode):
            if not rootNode:
                return 0
            print(rootNode.val)
            
            rightHeight = height(rootNode.right)
            leftHeight = height(rootNode.left)
            
            finalHeight = max(leftHeight, rightHeight) + 1
            
            if leftHeight + rightHeight > self.diam:
                self.diam = leftHeight + rightHeight
            
            return finalHeight
        
        if height(root.left) + height(root.right) > self.diam:
            self.diam = height(root.left) + height(root.right)
        
        return self.diam