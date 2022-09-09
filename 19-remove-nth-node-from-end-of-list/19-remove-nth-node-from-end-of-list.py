# Methodology -> Time, Space Complexity
# 1. Save to list, remove() -> O(N), O(N)
# 2. Count length of list, traverse to node and delete -> O(N), O(1)
# 3. Slow, fast pointers -> O(N), O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempHead = ListNode(0, head)
        left, right = tempHead, tempHead
        
        # Headstart
        for _ in range(n+1):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        
        return tempHead.next
            
        
            
        