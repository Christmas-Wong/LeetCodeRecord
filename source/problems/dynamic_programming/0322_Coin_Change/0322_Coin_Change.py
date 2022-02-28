# -*- coding: utf-8 -*-
"""
@Time       : 2022/2/28 10:05 PM
@Author     : Wang Fei
@Last Editor: Wang Fei
@Project    : LeetCodeRecord 
@File       : 0322_Coin_Change.py
@Software   : PyCharm
@Description: 
"""
import cProfile
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [0] + [float("inf")]*amount
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                result[i] = min(result[i], 1+result[i-coin])
        return result[amount] if result[amount] < float("inf") else -1


if __name__ == "__main__":
    solution = Solution()
    coins = [186, 419, 83, 408]
    amount = 6249
    cProfile.run("solution.coinChange(coins, amount)")
