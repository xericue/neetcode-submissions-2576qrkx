# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if both trees are None - return True in this base case
        if not p and not q:
            return True
        # check if one tree is None another is not OR 
        # if they have differing values - return False
        if not p or not q or p.val != q.val:
            return False

        # recursive step - if the and is True, then return True because
        # we want to know if both trees are equal - if both trees are not True, then it
        # will return false
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
