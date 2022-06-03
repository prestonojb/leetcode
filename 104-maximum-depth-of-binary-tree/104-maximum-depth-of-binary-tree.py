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
        self.updateDepth(root, 1)
        
        stack = []
        
        if root is None:
            return 0
        
        stack = [root]
        res = 0
        
        while len(stack) > 0:
            curr = stack.pop()
            
            if curr.depth > res:
                res = curr.depth
            
            if curr.left:
                stack += [curr.left]
                
            if curr.right:
                stack += [curr.right]
        
        return res
                            
    def updateDepth(self, tree_node, depth):
        if tree_node is None:
            return
        
        tree_node.depth = depth
        
        if tree_node.left:
            self.updateDepth(tree_node.left, depth + 1)
        if tree_node.right:
            self.updateDepth(tree_node.right, depth + 1)
        
        