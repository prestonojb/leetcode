# 1. Dictionary - O(n), O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if d.get(num) is None:
                d[num] = 1
            else:
                d[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in d.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res