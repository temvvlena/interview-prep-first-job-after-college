"""
Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
Time O(n*m) and Space (n*m) used an auxiliary array of size 
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while right > left and top < bottom:     
            # Let's go to the right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # Let's go to the downwards
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            if not (left<right and top<bottom): break
            # Let's go to the left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            # Go up
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
            
        
        
