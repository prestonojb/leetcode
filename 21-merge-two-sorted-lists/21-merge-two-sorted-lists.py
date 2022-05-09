# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 is None and list2 is None:
#             return None
        
#         if list1 is None and list2 is not None:
#             return list2
        
#         if list1 is not None and list2 is None:
#             return list1
        
#         p = list1
#         q = list2
#         head = list2
        
#         while p is not None and q is not None:
#             if p.val >= q.val:
#                 if q.next.val >= p.val:
#                     temp = p
#                     nxt = q.next
#                     q.next = p
#                     p.next = nxt
#                     p = temp.next
#                     q = q.next
#                 else:
#                     q = q.next
#             else:
#                 temp = p
#                 head = p
#                 p.next = q
#                 p = temp.next
        
#         return head
        l1 = list1
        l2 = list2
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next