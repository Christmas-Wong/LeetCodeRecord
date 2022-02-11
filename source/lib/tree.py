# -*- coding: utf-8 -*-
"""
@Time       : 2022/2/11 1:48 PM
@Author     : Wang Fei
@Last Editor: Wang Fei
@Project    : leetcode 
@File       : tree.py
@Software   : PyCharm
@Description: 
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def tree_from_array(array: List[int]) -> TreeNode:
    """ Transform A Array into Tree based on TreeNode
    Args:
        array: Source Array consist of int
    Returns:
        Root Node of a Tree
    Raises:
        None
    """

    if not array:
        return None
    result = TreeNode(array.pop(0))
    stack = [result]
    while stack and array:
        node = stack.pop(0)
        if not node:
            continue
        if array:
            num = array.pop(0)
            if num:
                node.left = TreeNode(num)
                stack.append(node.left)
            else:
                stack.append(None)
        if array:
            num = array.pop(0)
            if num:
                node.right = TreeNode(num)
                stack.append(node.right)
            else:
                stack.append(None)
    return result


def array_from_tree(root: Optional[TreeNode]) -> List[int]:
    """ Transform Tree into Array

    Args:
        root : Root Node of Tree
    Returns:
        Array of TreeNode Value by level traverse
    Raises:
        None
    """
    result = [root.val]
    stack = [root]
    while True and stack:
        for _ in range(len(stack)):
            node = stack.pop(0)
            if not node:
                result.append(None)
                continue
            else:
                result.append(node.val)
            if node.left:
                stack.append(node.left)
            else:
                stack.append(None)
            if node.right:
                stack.append(node.right)
            else:
                stack.append(None)
    while result and not result[-1]:
        result.pop(-1)
    return result

