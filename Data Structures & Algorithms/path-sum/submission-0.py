# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.path = []

        def psum(root, targetSum):
            # base case
            if not root:
                return False
            self.path.append(root.val)
            # check for leaf
            if not root.left and not root.right:
                if sum(self.path) == targetSum:
                    return True
                else:
                    self.path.pop()
                    return False
            if psum(root.left, targetSum):
                return True
            if psum(root.right, targetSum):
                return True
            self.path.pop()
            return False
            

        psum(root, targetSum)

        if not root or not self.path:
            return False
        return sum(self.path) == targetSum