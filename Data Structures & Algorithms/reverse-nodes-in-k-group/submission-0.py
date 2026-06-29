# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        # loop until it breaks naturally because k would exceed the limit
        while True:
            # find kth
            dummy_k = k
            kth = group_prev
            while kth and dummy_k > 0:
                kth = kth.next
                dummy_k -= 1
            
            if not kth:
                break

            # now, we have kth, and we can simply reverse an LL until we hit kth
            # SAVE the head of the next group
            group_next_head = kth.next # because kth was the last of our relevant group

            # reverse the current group
            # "prev" is actually gonna be the new head
            prev = group_next_head
            # curr is gonna be the current start
            curr = group_prev.next # not the old end of the last group, but the next node to it

            while curr != group_next_head: # curr is in bounds of the relevant group
                successor = curr.next
                curr.next = prev
                prev = curr # move prev up
                curr = successor

            # update the old start to the new start of the relevant group 
            tmp = group_prev.next # the old start of the unreversed group
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next