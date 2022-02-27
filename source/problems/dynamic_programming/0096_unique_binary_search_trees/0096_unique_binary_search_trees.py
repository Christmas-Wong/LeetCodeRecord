# -*- coding: utf-8 -*-
"""
@Time       : 2022/2/14 2:07 PM
@Author     : Wang Fei
@Last Editor: Wang Fei
@Project    : LeetCodeRecord 
@File       : 0096_unique_binary_search_trees.py
@Software   : PyCharm
@Description: 
"""
import cProfile


class Solution:
    def numTrees(self, n: int) -> int:
        list_result = [0]*(n+1)
        list_result[0] = 1
        list_result[1] = 1
        for ele in range(2, n+1):
            for item in range(1, ele+1):
                list_result[ele] += list_result[item-1]*list_result[ele-item]
        return list_result[n]


if __name__ == "__main__":
    solution = Solution()
    n = 5
    cProfile.run("solution.numTrees(n)")
