'''
Problem URL: https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 8
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def build_tree(self, start, end)->List[Optional[TreeNode]]:
    #     if start > end:
    #         return [None]
    #     all_trees = []
    #     for i in range(start, end + 1):
    #         # generate all left and right subtrees
    #         left_trees = self.build_tree(start, i - 1)
    #         right_trees = self.build_tree(i + 1, end)
    #         # combine left and right subtrees with the current root node
    #         for left in left_trees:
    #             for right in right_trees:
    #                 current_tree = TreeNode(i)
    #                 current_tree.left = left
    #                 current_tree.right = right
    #                 all_trees.append(current_tree)
    #     return all_trees
    # def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    #     if n == 0:
    #         return []
    #     return self.build_tree(1, n)





    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(l,r):
            if l>r:
                return [None]
            res=[]
            for i in range(l,r+1):
                for left in build(l,i-1):
                    for right in build(i+1,r):
                        node=TreeNode(i)
                        node.left=left
                        node.right=right
                        res.append(node)
            return res
        return build(1,n) 
    
    
    
    
    
    
    
    
    # def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # def generate_trees(start, end):
        #     if start > end:
        #         return [None,]
            
        #     all_trees = []
        #     for i in range(start, end + 1):
        #         left_trees = generate_trees(start, i - 1)
        #         right_trees = generate_trees(i + 1, end)
                
        #         for l in left_trees:
        #             for r in right_trees:
        #                 current_tree = TreeNode(i)
        #                 current_tree.left = l
        #                 current_tree.right = r
        #                 all_trees.append(current_tree)
            
        #     return all_trees
        
        # return generate_trees(1, n) if n else []




    #     if n == 0:
    #         return []

    #     dp = [[] for _ in range(n + 1)]
    #     dp[0].append(None)
    #     for nodes in range(1, n + 1):
    #         for root in range(1, nodes + 1):
    #             for left_tree in dp[root - 1]:
    #                 for right_tree in dp[nodes - root]:
    #                     root_node = TreeNode(root)
    #                     root_node.left = left_tree
    #                     root_node.right = self.clone(right_tree, root)
    #                     dp[nodes].append(root_node)
    #     return dp[n]
    
    # def clone(self, n: TreeNode, offset: int) -> TreeNode:
    #     if n:
    #         node = TreeNode(n.val + offset)
    #         node.left = self.clone(n.left, offset)
    #         node.right = self.clone(n.right, offset)
    #         return node
    #     return None






        # if n == 0:
        #     return []
        
        # memo = {}

        # def generate_trees(start, end):
        #     if (start, end) in memo:
        #         return memo[(start, end)]
            
        #     trees = []
        #     if start > end:
        #         trees.append(None)
        #         return trees
            
        #     for root_val in range(start, end + 1):
        #         left_trees = generate_trees(start, root_val - 1)
        #         right_trees = generate_trees(root_val + 1, end)
            
        #         for left_tree in left_trees:
        #             for right_tree in right_trees:
        #                 root = TreeNode(root_val, left_tree, right_tree)
        #                 trees.append(root)
            
        #     memo[(start, end)] = trees
        #     return trees

        # return generate_trees(1, n)







        # if n == 0:
        #     return []
        
        # from functools import lru_cache
        
        # @lru_cache(None)
        # def build(start, end):
        #     if start > end:
        #         return [None]
            
        #     trees = []
            
        #     for root_val in range(start, end + 1):
        #         left_trees = build(start, root_val - 1)
        #         right_trees = build(root_val + 1, end)
                
        #         for left in left_trees:
        #             for right in right_trees:
        #                 root = TreeNode(root_val)
        #                 root.left = left
        #                 root.right = right
        #                 trees.append(root)
            
        #     return trees
        
        # return build(1, n)




