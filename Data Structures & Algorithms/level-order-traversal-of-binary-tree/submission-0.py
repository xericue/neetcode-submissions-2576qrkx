# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # bfs uses an internal queue
        q = collections.deque() # python queue
        q.append(root)
    
        while q:
            # first, get the length of the queue since we'll always be requiring
            # the current level. This is how we can separate from B, C by screening
            # the array initially to getting D, E, F, G.
            qlen = len(q)
            new = [] # keep a level array
            for i in range(qlen):
                curr = q.popleft() # NOW get the first element because we got the initial
                # screen of how many elements we should be going for.
                # oh, hm; it makes sense to pop every node currently in the node in scope
                # of the lengths. you wouldnt just pop it after looking at it in this
                # specific problem because were trying to get every part of the level
                if curr:
                    new.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            
            # now, add the level IF ITS FINE
            if new:
                res.append(new)
        
        return res
        # basically, this is the crux of iterative bfs: start with a queue, add the root,
        # dequeue the node, do whatever, and add its children to the queue so you can 
        # keep doing so until the queue is finally empty
            




        return res

