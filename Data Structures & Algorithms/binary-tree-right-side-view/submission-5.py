# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # cant i just BFS**** this lol

        # think this would actually be best in bfs
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            qlen = len(q)
            for i in range(qlen):
                curr = q.popleft()
                # wait i popped in here? why?
                if curr:         
                    if i == qlen - 1:
                        res.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

        return res