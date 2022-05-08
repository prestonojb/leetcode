# Sorted in non-decreasing order
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        
        l, r = 0, len(numbers) - 1
        while l != r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum > target:
                r -= 1
            else:
                l += 1