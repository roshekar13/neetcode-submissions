# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        mid = (n+1)//2
        curr = head
        for i in range(mid-1):
            curr = curr.next
        
        cutoff = curr
        prev, curr = None, cutoff.next
        cutoff.next = None

        # reverse remainder of LL
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        
        # interleave starting at cutoff
        l,r = head, prev
        while l and r:
            temp1 = l.next
            temp2 = r.next

            l.next = r
            r.next = temp1

            l = temp1
            r = temp2

            

        



