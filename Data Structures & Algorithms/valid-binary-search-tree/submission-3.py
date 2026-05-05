# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.booly = True

        def vbst(root, left_interval, right_interval):
            if not root:
                return

            if left_interval >= root.val:
                self.booly = False
                return
            if right_interval <= root.val:
                self.booly = False
                return

            vbst(root.left, left_interval, root.val)
            vbst(root.right, root.val, right_interval)
    
        vbst(root, -float('inf'), float('inf'))
        return self.booly