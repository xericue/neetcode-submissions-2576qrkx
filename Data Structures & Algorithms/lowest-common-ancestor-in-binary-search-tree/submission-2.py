# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        # this fully works on a binary search tree because it traverses one level
        # at a time
        while curr:
            # if both values are greater than root, then go to the right
            # because the LCA will move from the tree's root to the subtree's root
            
            # this solution is not about traversing up from two found nodes;
            # we can leverage the fact that this is a BST (binary search tree)
            # and compare values until we find our LCA
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            else: # if our split occurs or if we actually find one of the values
            # this is essentially a catch all
                return curr
