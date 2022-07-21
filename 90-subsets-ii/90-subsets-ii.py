class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, cur):
            if i == len(nums):
                if sorted(cur) not in res:
                    res.append(sorted(cur[:]))
                return 

            cur.append(nums[i])
            dfs(i+1, cur)
            
            cur.pop()
            dfs(i+1, cur)
        
        dfs(0, [])
    
        return res