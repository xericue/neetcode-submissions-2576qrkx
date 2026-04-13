# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # so you wanna go left to right
        # O(n), O(n) space (because we have to put every node on the call stack)
        # create a nested function because we want to build our result
        result = []

        def inorder(root): # ingest a node
            if not root:
                return # dont do anything
            
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        
        return result

        # base case
        # [] + 
        
        # recursive case

        
        return result