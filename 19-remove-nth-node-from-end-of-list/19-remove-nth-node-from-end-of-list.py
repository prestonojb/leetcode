# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 1
        curr = head
        while curr.next:
            sz += 1
            curr = curr.next
            
        # sz = 5
        # n = 2
        
        if sz != n:
            # pos_to_delete = 4
            pos_to_delete = sz - n + 1
            curr = head
            for _ in range(1, pos_to_delete - 1):
                curr = curr.next

            prev = curr     
            node_to_delete = prev.next
            nxt = prev.next.next

            prev.next = nxt
            node_to_delete.next = None
        else:
            temp = head.next
            head.next = None
            head = temp
        
        return head