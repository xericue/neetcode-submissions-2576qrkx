# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret_str = []

        def dfs(root):
            if not root:
                ret_str.append("X")
                return
            
            ret_str.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(ret_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # first unpack it lol
        data_arr = data.split(",")
        self.i = 0 # some index, idk

        def dfs():
            # base case - if its invalid (deuh)
            if data_arr[self.i] == "X":
                self.i += 1
                return None

            # not null - create a TreeNode(int(data_arr[self.i]))
            node = TreeNode(int(data_arr[self.i]))
            self.i += 1
            node.left = dfs() # able to do so because we increment i
            node.right = dfs()
            return node
        return dfs()