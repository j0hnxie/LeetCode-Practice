# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        stack = deque()
        stack.append(root)
        depth = 0
        
        while stack:
            size = len(stack)
            for i in range(size):
                cur = stack.popleft()
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            
            depth += 1
            
        return depth
            
            