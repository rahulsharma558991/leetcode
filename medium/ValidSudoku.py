'''
Problem URL: https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = [[False] * 9 for _ in range(9)]
#         cols = [[False] * 9 for _ in range(9)]
#         boxes = [[False] * 9 for _ in range(9)]

#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] != '.':
#                     num = ord(board[i][j]) - ord('1')
#                     boxIndex = (i // 3) * 3 + (j // 3)
#                     if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
#                         return False
#                     rows[i][num] = cols[j][num] = boxes[boxIndex][num] = True
#         return True






# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         def get_subid(r, c):
#             if 0 <= r <= 2:
#                 if 0 <= c <= 2:
#                     return 0
#                 elif 3 <= c <= 5:
#                     return 1
#                 else:
#                     return 2
#             elif 3 <= r <= 5:
#                 if 0 <= c <= 2:
#                     return 3
#                 elif 3 <= c <= 5:
#                     return 4
#                 else:
#                     return 5
#             else:
#                 if 0 <= c <= 2:
#                     return 6
#                 elif 3 <= c <= 5:
#                     return 7
#                 else:
#                     return 8

#         m = len(board)
#         n = len(board[0])
#         rows = [set() for _ in range(m)]
#         cols = [set() for _ in range(n)]
#         subs = [set() for _ in range(9)]

#         for r in range(m):
#             for c in range(n):
#                 curr = board[r][c]
#                 if curr == '.':
#                     continue
#                 subid = get_subid(r, c)
#                 if curr in rows[r] or curr in cols[c] or curr in subs[subid]:
#                     return False
#                 rows[r].add(curr)
#                 cols[c].add(curr)
#                 subs[subid].add(curr)
#         return True









# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:

#         row_sets = [set() for _ in range(9)]
#         column_sets = [set() for _ in range(9)]
#         box_sets = [set() for _ in range(9)]

#         for i, row in enumerate(board):
#             for j, elem in enumerate(row):
                
#                 if elem == ".":
#                     continue

#                 k = i//3 * 3 + j//3

#                 if elem in row_sets[i] or elem in column_sets[j] or elem in box_sets[k] :
#                     return False
                
#                 row_sets[i].add(elem)
#                 column_sets[j].add(elem)
#                 box_sets[k].add(elem)

#         return True












class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_map = defaultdict(list)
        c_map = defaultdict(list)
        b_map = defaultdict(list)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in r_map[r] or board[r][c] in c_map[c] or board[r][c] in b_map[(r//3,c//3)]:
                    return False
                else:
                    r_map[r].append(board[r][c])
                    c_map[c].append(board[r][c])
                    b_map[(r//3,c//3)].append(board[r][c])
        return True