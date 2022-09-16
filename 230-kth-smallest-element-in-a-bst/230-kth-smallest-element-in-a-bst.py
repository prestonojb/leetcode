# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:    
# 1. Inorder Traversal (Recursive) 
#         def inorder(root, output):
#             if root is None:
#                 return

#             inorder(root.left, output)
#             output.append(root)
#             inorder(root.right, output)
            
#         output = []
#         inorder(root, output)
        
#         return output[k-1].val

# 2. Inorder traversal (Iterative)
        stack = []
        curr = root
    
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                
                k -= 1
                if k == 0:
                    return curr.val
                
                curr = curr.right