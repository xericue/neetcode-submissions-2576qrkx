# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.booly = True

        def bbt(node):
            if not node:
                return 0
            
            left = bbt(node.left)
            right = bbt(node.right)
            if abs(left - right) > 1:
                self.booly = False
                return 0
        
            return 1 + max(left, right)

        bbt(root)
        return self.booly
        