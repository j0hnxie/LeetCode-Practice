# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        queue = deque()
        queue.append(root)
        result = []
        if not root:
            return result
        
        while queue:
            lvl = len(queue)
            result.append([])
            
            for i in range(lvl):
                top = queue.popleft()
                if top.left:
                    queue.append(top.left)
                
                if top.right:
                    queue.append(top.right)
                result[-1].append(top.val)
        
        return result
            
            