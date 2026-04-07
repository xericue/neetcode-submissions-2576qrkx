# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = sentinel = ListNode()

        while list1 and list2 and curr:
            if list1.val >= list2.val:
                temp = list2.next
                curr.next = list2
                list2 = temp
                
            else:
                temp = list1.next
                curr.next = list1
                list1 = temp
            curr = curr.next
        
        curr.next = list1 or list2

        return sentinel.next