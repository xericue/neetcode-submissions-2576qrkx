# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # up here, we check our base cases
        if not subRoot:
            return True # because itll be a leaf node null thats a sub tree
        if not root:
            return False # because t cant be a subtree of nothing

        # now we check if the roots are similar/the same tree
        if self.same_tree(root, subRoot):
            return True
        
        # otherwise, recurse - we want an EVENTUALY match of either the left or the
        # right, so we can just compare t (the subtree) to the entire left of s or
        # to the entire right of s

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same_tree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            # compare the rset of the sub trees recursively
            # since we're looking for completely identical trees, this has
            # to return true for the left AND right subtrees
            return self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right)
        else: # otherwise, one tree is null and one tree is non-null
            return False