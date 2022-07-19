class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        pos = 0
        dest_idx = len(nums) - 1
        while pos < dest_idx:
            jump_len = nums[pos]
            greedy_land_idx = -1
            for land_idx in range(pos + 1, pos + jump_len + 1):
                if land_idx == dest_idx:
                    return res + 1
                jump_dist = land_idx - pos
                nxt_jump_len = nums[land_idx]
                score = jump_dist + nxt_jump_len
                greedy_land_idx_score = greedy_land_idx - pos + nums[greedy_land_idx]
                if greedy_land_idx == -1 or score > greedy_land_idx_score:
                    greedy_land_idx = land_idx
            pos = greedy_land_idx
            res += 1
        return res
        
                
                