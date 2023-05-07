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
        
#         stack = deque()
        
#         if root != None:
#             stack.append(root)
        
#         while stack:
            
            
            
        
        def height(node):
            if node == None:
                return 0
            left = height(node.left)
            
            if left == -1:
                return -1
            
            right = height(node.right)
            
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        # if root == None:
        #     return True
        
        return height(root) != -1