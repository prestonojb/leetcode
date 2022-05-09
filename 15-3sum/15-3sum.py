# Requirements:
# - Distinct i,j,k
# - No duplicate [i,j,k]
# - nums[i]+nums[j]+nums[k] == 0

# Brute force - O(N^3)
#         res = []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i != j:
#                     for k in range(len(nums)):
#                         if i != k and j != k:
#                             if nums[i] + nums[j] + nums[k] == 0:
#                                 res.append([nums[i],nums[j],nums[k]])
        
#         output = []
#         for i in range(len(res)):
#             sorted_triplets = sorted(res[i])
#             if sorted_triplets not in output:
#                 output.append(sorted_triplets)

#         return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []

        # Sort array in non-decreasing order - O(N log N) + Two Sum - O(N^2)
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        res = []
        
        for i in range(n):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
                
            l,r = i+1,n-1
            while l<r:
                three_sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if three_sum == 0:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    while l<r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
            
        return res    