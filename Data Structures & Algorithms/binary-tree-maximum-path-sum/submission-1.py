# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = [root.val] # base case
        # its a list 

        def dfs(node):
            if not node:
                return 0
            
            # these are compared with 0 in case theyre negative
            # and its 0 because if we DO add it to a future sum it adds nothing
            leftmax = max(dfs(node.left), 0)
            rightmax = max(dfs(node.right), 0)

            # now that we haave the maxes, calculate the path as if this was
            # our root node and we wanted to update our glomax with this path
            total[0] = max(total[0], node.val + leftmax + rightmax)

            # OTHERWISE! calculate the best without a split and return it up
            return node.val + max(leftmax, rightmax)

        dfs(root)
        return total[0]