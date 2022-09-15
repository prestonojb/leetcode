class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            dfs(i, cur + [candidates[i]], total + candidates[i])
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res