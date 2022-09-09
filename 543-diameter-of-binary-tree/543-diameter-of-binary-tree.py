# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if root is None:
                return -1
            
            leftHeight = dfs(root.left) + 1
            rightHeight = dfs(root.right) + 1
            
            res[0] = max(res[0], leftHeight + rightHeight)
            
            return max(leftHeight, rightHeight)
        
        dfs(root)
        return res[0]