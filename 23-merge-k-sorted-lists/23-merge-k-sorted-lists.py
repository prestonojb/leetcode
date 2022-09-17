# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        minHeap = []
        
        for head in lists:
            if not head:
                continue

            curr = head
            while curr:
                heapq.heappush(minHeap, curr.val)
                curr = curr.next
                
        if len(minHeap) == 0:
            return None
        
        prev = None
        prev_node = None
        head = heapq.heappop(minHeap)
        head_node = ListNode(head)
        curr = head
        curr_node = head_node
        
        while minHeap:
            prev = curr
            prev_node = curr_node
            
            curr = heapq.heappop(minHeap)
            curr_node = ListNode(curr)
            
            prev_node.next = curr_node
        
        return head_node