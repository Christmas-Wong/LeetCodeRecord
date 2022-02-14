# -*- coding: utf-8 -*-
"""
@Time       : 2022/2/11 2:56 PM
@Author     : Wang Fei
@Last Editor: Wang Fei
@Project    : leetcode 
@File       : base.py
@Software   : PyCharm
@Description: 
"""
import cProfile


def is_prime(n: int):
    limit = int(n**0.5)+1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


class Solution:
    def countPrimes(self, n: int) -> int:
        result = 0
        for i in range(2, n):
            if is_prime(i):
                result += 1
        print(result)
        return result


if __name__ == "__main__":
    n = 10
    solution = Solution()
    cProfile.run("solution.countPrimes(n)")
