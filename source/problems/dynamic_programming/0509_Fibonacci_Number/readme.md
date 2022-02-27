# [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
## Problem
求斐波那切数列第n个数
## Solution
- 起始状态
  - n=0，result=0
  - n=1, result=1
- 迭代公式
  - 迭代公式
```
第n个数=第n-1个数+第n-2个数
```

## Summary
- 有两种用空间换时间的方法
  - 第一种：用数组存储每个位置的数字，每次迭代直接取对应位置即可
  - 第二种：只存储每次迭代所需要的两个数字，但是需要在每次迭代的时候更新