"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/solution/
N-ary Tree Postorder Traversal
Given an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).
Follow up:
Recursive solution is trivial, could you do it iteratively?
Example 1
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
Time and Space O(N)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        stack, output = [root, ], []  
        while stack:
            root = stack.pop()
            if root is not None: output.append(root.val)
            for c in root.children: stack.append(c)
        return output[::-1]
        """
        res = []
        def helper(root):
            if root is None: return
            for i in root.children: helper(i)
            res.append(root.val)
        helper(root)
        return res
        """