# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False    
        
        walker = head.next
        runner = head.next.next
        
        while walker and runner:
            if walker == runner:
                return True
            walker = walker.next
            runner = runner.next.next if runner.next else None
            
        
        return False
        
        