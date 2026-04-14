# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive call where you switch Uh ohhhh UHhhhhhhhh DAMN IT!
        res = []

        if not root:
            res.append(root)
            return None

        self.invertTree(root.left)
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)

        return root