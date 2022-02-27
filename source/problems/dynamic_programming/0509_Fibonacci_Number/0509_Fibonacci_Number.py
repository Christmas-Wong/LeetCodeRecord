# -*- coding: utf-8 -*-
"""
@Time       : 2022/2/27 10:33 PM
@Author     : Wang Fei
@Last Editor: Wang Fei
@Project    : LeetCodeRecord 
@File       : 0509_Fibonacci_Number.py
@Software   : PyCharm
@Description: 
"""
import cProfile


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        numbers = [0]*(n+1)
        numbers[0] = 0
        numbers[1] = 1
        for i in range(2, n+1):
            numbers[i] = numbers[i-1] + numbers[i-2]
        return numbers[n]

    def fib_2(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        while n >= 2:
            result = a + b
            a, b = b, result
            n -= 1
        return result


if __name__ == "__main__":
    n = 100000
    solution = Solution()
    cProfile.run("solution.fib(n)")
    cProfile.run("solution.fib_2(n)")
