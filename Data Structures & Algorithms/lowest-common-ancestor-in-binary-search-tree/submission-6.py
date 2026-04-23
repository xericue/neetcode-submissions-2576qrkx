# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # because this is a BST you can. Literally just use binary search

        # HOWEVRE!
        # if you think about it, what the LCA is of two nodes in a BST is the split
        # 3 and 8 -> 5 splits them. 4 and 7 -> 5 splits them. 8 and 9 -> 8 splits them
        # so we can define an easy binary search here

        while root:
            # our initial conditions can actually be if the root is [l|g]t BOTH of them.
            # think about it - if our current node is lt both of them, then we'll need
            # to go to the right node to try bs again because this is a bst - every
            # left is lt and every right is gt
            if p.val == root.val or q.val == root.val:
                return root
            if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
                return root
            
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                root = root.left
        return root