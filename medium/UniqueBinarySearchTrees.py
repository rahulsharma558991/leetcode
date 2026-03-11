'''
Problem URL: https://leetcode.com/problems/unique-binary-search-trees/description

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 19
'''

# class Solution:
#     def numTrees(self, n: int) -> int:
#         if n <= 1: return 1
#         return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))





# class Solution:
#     @cache
#     def numTrees(self, n: int) -> int:
#         if n <= 1: return 1
#         return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))






# class Solution:
#     def numTrees(self, n: int) -> int:
#         dp = [0]*(n+1)
#         dp[0], dp[1] = 1, 1
#         for i in range(2, n+1):
#             for j in range(1, i+1):
#                 dp[i] += dp[j-1] * dp[i-j]
#         return dp[n]






# class Solution:
#     def numTrees(self, n: int) -> int:
#         return factorial(2*n) // (factorial(n)*factorial(n+1))




class Solution:
    def numTrees(self, n: int) -> int:

        # Approach 1
        @lru_cache(None)
        def dfs(l, r):
            if l == r:
                return 1
            res = 0
            for i in range(l, r):
                res += dfs(l, i) * dfs(i + 1, r)
            return res

        return dfs(0, n)