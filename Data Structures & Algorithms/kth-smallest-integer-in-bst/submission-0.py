# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.total = 0
        self.ans = 0

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            self.total += 1
            if self.total == k:
                self.ans = root.val
            inorder(root.right)

            return

        # def bst(root, n):
        #     if k == n:
        #         return root.val
        #     elif k < n:
        #         bst(root, n / 2)
        #     else:
        #         bst(root, n * 1.5)

            
        inorder(root)
        return self.ans  