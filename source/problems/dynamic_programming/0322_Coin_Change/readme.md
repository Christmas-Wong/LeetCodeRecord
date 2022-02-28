# [Coin Change](https://leetcode.com/problems/coin-change/)
## Problem
给定一个零钱列表和总钱数，返回最小找钱数量
## Solution
- 起始状态
  - n=0，result=0
- 迭代公式
  - 迭代公式
```
遍历从0到amount之间的每一个总钱数
第i个结果等于第i-1的结果加一，或者凑不出来
```

## Summary
