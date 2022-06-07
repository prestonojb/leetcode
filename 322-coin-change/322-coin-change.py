class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None] * (amount + 1)
        memo[0] = 0
        for i in range(1, len(memo)):
            ex_min_coins = float("inf")
            for coin in coins:
                if (i - coin) >= 0 and memo[i-coin] >= 0:
                    ex_min_coins = min(memo[i-coin], ex_min_coins)
            if ex_min_coins == float("inf"):
                memo[i] = -1
            else:
                memo[i] = ex_min_coins + 1
        
        return memo[-1]