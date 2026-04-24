# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we need to pass in more than just the root, so you may define a helper w/ max
        def dfs(node, maxVal):
            if not node:
                return 0
            
            # is this a good node - check and update. one full block of two operations
            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            
            maxVal = max(maxVal, node.val)

            # now, recursive calls
            # so the reason this is preorder is because we're processing each node first
            # before passing it along because maxVal needs to consider the current node.
            left = dfs(node.left, maxVal)
            right = dfs(node.right, maxVal)
            return res + left + right
        
        return dfs(root, root.val)