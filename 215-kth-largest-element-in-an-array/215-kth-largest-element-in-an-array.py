class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sort array - O(n log n)
        # MaxHeap - O(n)
        inverted_nums = [-n for n in nums]
        
        heapq.heapify(inverted_nums)
        
        for _ in range(k-1):
            heapq.heappop(inverted_nums)
        
        return -(heapq.heappop(inverted_nums))
        