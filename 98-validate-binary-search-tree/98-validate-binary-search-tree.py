# 1. Recursion
# 2. Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        stack = []
        curr = root
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                arr.append(curr.val)
                curr = curr.right
        
        return arr == sorted(arr) and len(arr) == len(set(arr))