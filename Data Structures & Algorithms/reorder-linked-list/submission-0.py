# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # second half of the list
        slow.next = None # split into two diff lists

        # now reverse the second half of the list
        # set a previous node/predecessor
        predecessor = None
        while second:
            # set it to the previous nodes - remember from reversing
            # predecessor, node, successor
            curr = second.next
            second.next = predecessor
            predecessor = second
            second = curr
            # this is the iterative way to reverse a linked list

        # now merge the two halves
        # second is None, but remember to set it equal to prev so that its
        # the actual last node
        first = head
        second = predecessor

        while second:
            temp_first = first.next # because youre breaking the first and first.next link
            temp_second = second.next # breaking second and second.next

            # merging operation
            first.next = second
            second.next = temp_first

            # fixing pointers
            first = temp_first
            second = temp_second
            