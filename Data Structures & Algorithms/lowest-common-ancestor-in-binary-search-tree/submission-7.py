# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # because this is a BST you can. Literally just use binary search

        while root:
            # bst - every left is lt and every right is gt
            if p.val == root.val or q.val == root.val:
                return root
            if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
                return root
            
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                root = root.left
        return root