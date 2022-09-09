# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Parent node = good node
        # curr node >= parent node -> good
        # curr node < parent node -> x good
        
        # Parent node = x good node
        # traverse up until you find a good node
        # compare if curr node >= immediate parent good node -> good
        # else no
        
        # dfs (*)
        # bfs
        res = [0]
        
        def dfs(root, limit):
            if root is None:
                return
            if root.val >= limit:
                res[0] += 1
                limit = root.val
            
            dfs(root.left, limit)
            dfs(root.right, limit)
        
        dfs(root, root.val)
        return res[0]
            
            
            
            