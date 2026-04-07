# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        f_map = {}

        while curr:
            if curr in f_map:
                return True
            
            f_map[curr] = 1
            curr = curr.next

        return False