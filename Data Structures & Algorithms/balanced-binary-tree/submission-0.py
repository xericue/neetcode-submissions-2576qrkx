# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.booly = True

        def helper(root):
            if not root:
                return 0

            ld = helper(root.left)
            rd = helper(root.right)

            if abs(ld - rd) > 1:
                self.booly = False
                return 0
            
            return 1 + max(ld, rd)
        
        # do something on left
        # do something on right

        helper(root)
        return self.booly