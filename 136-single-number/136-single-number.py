# 1. Brute force
# 2. Dictionary 
# 3. Sorted array
# 4. XOR (optimized)
#    x ^ x = 0
#    For duplicate elements in list, nullify to 0, left is the unduplicated element

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
        