class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(pos, cur, total):
            if target == total:
                res.append(cur[:])
                return
            if total > target or pos >= len(candidates):
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                cur.append(candidates[i])
                dfs(i+1, cur, total + candidates[i])
                prev = cur.pop()
        
        dfs(0, [], 0)
        return res