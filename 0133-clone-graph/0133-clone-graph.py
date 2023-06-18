"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        dfs = []
        if node:
            dfs.append(node)
        else:
            return None
        
        visited = set()
        visited.add(node.val)
        thisDict = {node.val: Node(val = node.val)}
        result = thisDict[node.val]
        
        while dfs:
            top = dfs[-1]
            cur = thisDict[top.val]
            dfs.pop()
            for i in top.neighbors:
                if not i.val in visited:
                    dfs.append(i)
                    visited.add(i.val)
                    created = Node(val = i.val)
                    thisDict[i.val] = created
                    cur.neighbors.append(created)
                else:
                    cur.neighbors.append(thisDict[i.val])
            
        return result
                
            