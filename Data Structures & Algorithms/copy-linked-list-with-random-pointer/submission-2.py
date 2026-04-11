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
        
        mappings = {None : None}
        
        curr = head
        while curr:
            new_node = Node(curr.val)
            # mapping the old node to the new code
            mappings[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            mappings[curr].next = mappings[curr.next]
            mappings[curr].random = mappings[curr.random]
            curr = curr.next
            
        curr = head
        return mappings[curr]

