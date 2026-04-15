# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # so you HAVE to declare this as inherent to the class otherwise
        # the local scope of the helper function will always lose it/update
        # something else
        self.result = 0

        def dfs(root):

            if not root:
                return 0

            ld = dfs(root.left)
            rd = dfs(root.right)
        
            self.result = max(ld + rd, self.result)
            return 1 + max(ld, rd)

        dfs(root)
        return self.result