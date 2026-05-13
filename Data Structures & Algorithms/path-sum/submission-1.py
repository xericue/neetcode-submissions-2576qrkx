# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.path = []

        def dfs(root, targetSum):
            # base case
            if not root:
                return False
            
            # append valid node
            self.path.append(root.val)

            # recursive cases
            if not root.left and not root.right:
                if sum(self.path) == targetSum:
                    return True
                self.path.pop()
                return False
            
            # make it through not being a leaf - this is a regular node
            # we recurse left and if it returns True then return True 
            if dfs(root.left, targetSum):
                return True
            # we recurse right and if it returns True then return True 
            if dfs(root.right, targetSum):
                return True

            # otherwise, we've made it past all of our conditions - this is an invalid node/path
            # because it hasn't returned yet
            self.path.pop()
            return False
            

        dfs(root, targetSum)
        if not self.path:
            return False
        if sum(self.path) == targetSum:
            print(self.path)
            return True

        return False
        