# 1. Brute force
# 2. Bit manipulation
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # Remove last 1 
        while n:
            n &= (n-1)
            count += 1
        return count        