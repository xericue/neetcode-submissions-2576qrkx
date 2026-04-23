# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            # we're going to be returning a numerical value
            if not root:
                return 0
            # i think this one legitimately needs to use max() because, when we go down
            # each subtree, we're going to need to take the maximum value from both
            # and compare the two to return the real maximum

            left = dfs(root.left)
            right = dfs(root.right)

            return 1 + max(left, right)

        ret = dfs(root)
        return ret