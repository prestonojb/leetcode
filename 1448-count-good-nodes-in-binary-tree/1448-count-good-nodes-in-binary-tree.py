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
        
        def dfs(root, immediate_good_parent_node_val):
            if root.val >= immediate_good_parent_node_val:
                res[0] += 1
                immediate_good_parent_node_val = root.val
            
            if root.left:
                dfs(root.left, immediate_good_parent_node_val)
            if root.right:
                dfs(root.right, immediate_good_parent_node_val)
            
        dfs(root, root.val)
        return res[0]