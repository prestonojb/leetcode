# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        
        def dfs(parent):
            if parent is None:
                return float("-inf")
            if parent.left is None and parent.right is None:
                res[0] = max(res[0], parent.val)
                return parent.val
            
            left_path_sum = dfs(parent.left)
            right_path_sum = dfs(parent.right)
            left_right_path_sum = left_path_sum + right_path_sum + parent.val
            
            mps = max(parent.val, left_path_sum + parent.val, right_path_sum + parent.val)
            res[0] = max(res[0], left_right_path_sum, left_path_sum, right_path_sum, mps)
            
            return mps
        
        dfs(root)
        return res[0]