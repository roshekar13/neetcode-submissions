# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val_set = set()
        temp = head
        while temp != None:
            print(temp.val)
            if temp.val in val_set:
                if temp.next != None:
                    return True
                else:
                    print('ahsda')
                    print(temp.val)
                    return False
            else:
                val_set.add(temp.val)
            temp = temp.next
        return False