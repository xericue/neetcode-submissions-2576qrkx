"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_to_new_mapping = {None : None} # map None to None in case of randoms and nexts
        
        curr = head
        while curr:
            # new node
            new = Node(curr.val)

            # map old to new in map
            old_to_new_mapping[curr] = new
            curr = curr.next

        # move curr back to head
        curr = head
        while curr:
            # get our new node ready for usage
            new = old_to_new_mapping[curr]
            new.next = old_to_new_mapping[curr.next]
            new.random = old_to_new_mapping[curr.random]
            curr = curr.next

        # use head (old node) to index new head
        return old_to_new_mapping[head]