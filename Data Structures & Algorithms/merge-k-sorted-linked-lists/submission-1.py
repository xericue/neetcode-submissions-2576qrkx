# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # since, at every step, we want some minimum, a heap is appropriate
        heap = []

        # append all initial node references, as the list gives us
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap) # unpack
            curr.next = node # because it was the minimum
            curr = node # move curr ptr to... the node? not curr.next?
            node = node.next # move to next reference
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return dummy.next