# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def helper(self, root, depth):
#         self.maxDepth = max(self.maxDepth, depth)
#         if not root:
#             return depth
#         left = self.helper(root.left, depth+1)
#         right = self.helper(root.right, depth+1)
#         if left == right == self.maxDepth:
#             self.res = root
#         return max(left, right)
    
#     def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         if not root:
#             return None
#         self.res = None
#         self.maxDepth = -1
#         self.helper(root, 0)
#         return self.res

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxDepth = [-1]
        res = [None]
        
        if not root:
            return None
        
        def dfs(root, depth):
            maxDepth[0] = max(maxDepth[0], depth)
            if not root:
                return depth
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)
            if left == right == maxDepth[0]:
                res[0] = root
            return max(left, right)
        
        dfs(root, 0)
        return res[0]