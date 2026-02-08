'''
Problem URL: https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced.
Height-Balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     return self.height(root) != -1

    # def height(self, node: TreeNode) -> int:
    #     if not node:
    #         return 0  # Base case: empty tree has height 0
        
    #     # Recursively get the height of the left subtree
    #     left_height = self.height(node.left)
    #     if left_height == -1:
    #         return -1  # If the left subtree is unbalanced, return -1

    #     # Recursively get the height of the right subtree
    #     right_height = self.height(node.right)
    #     if right_height == -1:
    #         return -1  # If the right subtree is unbalanced, return -1
        
    #     # If the height difference between left and right subtrees is more than 1, return -1
    #     if abs(left_height - right_height) > 1:
    #         return -1
        
    #     # Return the height of the current node
    #     return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node):
            if node is None:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if abs(l-r) > 1:
                self.balanced = False

            return max(l,r) + 1
        dfs(root)
        return self.balanced   
    