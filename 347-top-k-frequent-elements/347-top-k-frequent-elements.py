# 1. Bucket/Dictionary - O(n), O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            d[num] = 1 + d.get(num, 0)
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in d.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res