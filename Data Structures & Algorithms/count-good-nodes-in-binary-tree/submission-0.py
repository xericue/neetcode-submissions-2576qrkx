# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # keep the maximum value every time you return up
        def dfs(root, maxVal):
            if not root:
                return 0

            res = 0
            if root.val >= maxVal:
                res = 1
            maxVal = max(maxVal, root.val)
            left = dfs(root.left, maxVal)
            right = dfs(root.right, maxVal)
            return res + left + right

        full_res = dfs(root, root.val)
        return full_res