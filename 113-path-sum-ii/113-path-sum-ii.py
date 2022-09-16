# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if not root: 
                return
            
            targetSum -= root.val
            
            path.append(root.val)
            if not root.left and not root.right:  # Is leaf node
                if targetSum == 0:  # Found a valid path
                    res.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack

        res = []
        dfs(root, targetSum, [])
        return res