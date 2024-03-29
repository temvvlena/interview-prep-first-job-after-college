"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
N-ary Tree Preorder Traversal
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
Follow up:

Recursive solution is trivial, could you do it iteratively?
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):                 
        if root is None: return []
        res = []
        res.append(root.val)
        children = root.children
        for i in range(len(children)): 
            temp = self.preorder(children[i])
            for i in temp: res.append(i)
        return res
        """
        if root is None: return []
        myStack, res = [root], []
        while myStack:
            cur = myStack.pop()
            res.append(cur.val)
            children = cur.children
            myLength = len(children) - 1
            while myLength >= 0:
                myStack.append(children[myLength])
                myLength -= 1
        return res
        """
