# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        if left == 1:
            left_endpoint = None
            start_of_sorted_portion = head
        else:
            left_endpoint = head
            for _ in range(left-1-1):
                left_endpoint = left_endpoint.next
            start_of_sorted_portion = left_endpoint.next

        right_endpoint = head
        for _ in range(right):
            right_endpoint = right_endpoint.next
            
        prev = None
        curr = start_of_sorted_portion
        
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        if left_endpoint:
            left_endpoint.next = prev
        start_of_sorted_portion.next = right_endpoint
        
        return head if left_endpoint else prev