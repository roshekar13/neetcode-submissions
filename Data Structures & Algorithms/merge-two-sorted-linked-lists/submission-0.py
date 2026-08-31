# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2
        head = ListNode(0)
        new = head
        #while i-1 != List
        while i != None and j != None:
            if i.val <= j.val:
                new.next = i
                i = i.next
            else:
                new.next = j
                j = j.next
            new = new.next
        if i:
            new.next = i
        else:
            new.next = j
        
        return head.next

        
