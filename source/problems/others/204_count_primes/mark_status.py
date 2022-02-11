# -*- coding: utf-8 -*-
"""
@Time       : 2022/2/11 1:51 PM
@Author     : Wang Fei
@Last Editor: Wang Fei
@Project    : leetcode 
@File       : mark_status.py
@Software   : PyCharm
@Description: 
"""
import cProfile


class SolutionBase:
    def countPrimes(self, n: int) -> int:
        not_prime = [1]*n
        not_prime[0] = not_prime[1] = 0
        for i in range(2, n):
            if not_prime[i] == 1:
                j = 2
                while i*j < n:
                    not_prime[i*j] = 0
                    j += 1
        print(sum(not_prime))
        return sum(not_prime)


class SolutionImprove:
    def countPrimes(self, n: int) -> int:
        not_prime = [1]*n
        not_prime[0] = not_prime[1] = 0
        limit = int(n ** 0.5)+1
        for i in range(2, limit):
            if not_prime[i] == 1:
                not_prime[i*i: n: i] = [0] * len(not_prime[i*i: n: i])
        print(sum(not_prime))
        return sum(not_prime)


if __name__ == "__main__":
    n = 10
    solution = SolutionBase()
    cProfile.run("solution.countPrimes(n)")


