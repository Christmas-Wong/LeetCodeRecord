# [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)
## Problem
给定一个正整数n, 求[1, n]能够组成多少个二叉搜索树
## Solution
- 起始状态
  - n=0，result=1
  - n=1, result=1
- 迭代公式
  - 迭代公式
```
定义以i为root的二叉搜索树的数量为f(i)
定义[0, i]组成的二叉搜索树的数量为g(i)
那么[0, n]中以i为root的二叉搜索树的数量为：f(i) = g(i)*g(n-i)
那么[0, n]可以组成的二叉搜索树数量为sum(f(i))
```

## Summary
- 分析g(n-i)
```
二叉搜索树的构建构建的核心依据是节点之间的大小比较，与具体数值无关
所以g{i, n}其实与g{0, n-i}的二叉搜索树数量一致(每个节点数值减去i即可)
```