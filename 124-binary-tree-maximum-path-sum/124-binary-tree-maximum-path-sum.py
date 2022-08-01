# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        memo = {}
        
        def dfs(parent):
            if parent is None:
                return float("-inf")
            if parent.left is None and parent.right is None:
                res[0] = max(res[0], parent.val)
                memo[parent] = parent.val
                return memo[parent]
            
            if memo.get(parent.left) is None:
                memo[parent.left] = dfs(parent.left)
            if memo.get(parent.right) is None:
                memo[parent.right] = dfs(parent.right)
            
            left_path_sum = memo[parent.left]
            right_path_sum = memo[parent.right]
            left_right_path_sum = memo[parent.left] + memo[parent.right] + parent.val
            
            memo[parent] = max(parent.val, left_path_sum + parent.val, right_path_sum + parent.val)
            res[0] = max(res[0], left_right_path_sum, left_path_sum, right_path_sum, memo[parent])
            
            return memo[parent]
        
        dfs(root)
        return res[0]