'''
Problem URL: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

Constraints:
n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
'''

# class Solution:
#     def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # m = len(mat)
        # n = len(mat[0])

        # for _ in range(4):
        #     # Step 1: Transpose
        #     for i in range(m):
        #         for j in range(i, n):
        #             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        #     # Step 2: Reverse each row
        #     for row in mat:
        #         row.reverse()
        #     # Check if equal
        #     if mat == target:
        #         return True
        # return False





# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#                     # transpose
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         for row in matrix:
#             row.reverse()

#     def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
#         for _ in range(4):
#             if mat == target:
#                 return True
#             self.rotate(mat)
#         return False





# class Solution:
#     def rotate90(self, matrix):
#         n , m = len(matrix), len(matrix[0])
#         rotated_mat = []

#         for i in range(m):
#             row = []
#             for j in range(n):
#                 row.append(matrix[j][i])
#             rotated_mat.append(row[::-1])

#         return rotated_mat


#     def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
#         # 90 deg
#         mat1 = self.rotate90(mat)
#         # 180 deg
#         mat2 = self.rotate90(mat1)
#         #  270 deg
#         mat3 = self.rotate90(mat2)

#         return mat == target or mat1 == target or mat2 == target or mat3 == target






class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_90_clockwise(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for row in matrix:
                row.reverse()
        for i in range(4):
            if mat == target:
                return True
            rotate_90_clockwise(mat)
        return False
