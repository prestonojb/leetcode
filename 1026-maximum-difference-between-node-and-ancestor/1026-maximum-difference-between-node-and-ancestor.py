# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        def dfs(node, high, low):
            if not node:
                return high - low
            high = max(high, node.val)
            low = min(low, node.val)
            return max(dfs(node.left, high, low), dfs(node.right,high,low))
    
        return dfs(root, root.val, root.val)