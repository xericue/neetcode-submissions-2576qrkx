# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # always start w base case for recrusion
        if not preorder or not inorder:
            return None
        
        # cant do this recursively
        # if preorder == inorder: # comparing list values/[1] to [1], not addresses
        #     return TreeNode(preorder[0])
        
        # start building recursive case

        root = TreeNode(preorder[0])
        # cut = 0
        # for i, v in enumerate(inorder):
        #     if v == root.val:
        #         cut = i
        #         break

        # you can apparently do this with inorder.index(preorder[0]), but whatever
        cut = inorder.index(preorder[0])

        # start building the subtree RECURSIVELY
        # cut tells us how many nodes we WANT in the left subtree
        # so skip the 0th index and then go up plus 1 - cut is the index
        # then for index, itll be from the beginning up until but not includinng cut
        root.left = self.buildTree(preorder[1:cut + 1], inorder[:cut])

        # then for right, we need every value AFTER cut + 1
        # and then for inorder, we're gonna be looking at the same thing
        root.right = self.buildTree(preorder[cut + 1:], inorder[cut + 1:])

        # so now the root index inside of the inorder array is where it should be type shrimp


        return root
