'''
Problem URL: https://leetcode.com/problems/climbing-stairs/description

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
'''

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return 1
#         return self.climbStairs(n-1) + self.climbStairs(n-2)




# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {}
#         return self.helper(n, memo)
    
#     def helper(self, n: int, memo: dict[int, int]) -> int:
#         if n == 0 or n == 1:
#             return 1
#         if n not in memo:
#             memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
#         return memo[n]





# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return 1

#         dp = [0] * (n+1)
#         dp[0] = dp[1] = 1
        
#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]






# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return 1
#         prev, curr = 1, 1
#         for i in range(2, n+1):
#             temp = curr
#             curr = prev + curr
#             prev = temp
#         return curr







class Solution:
    def climbStairs(self, n: int) -> int:
        # lets try pulld dp
        if n <= 2:
            return n
        first_step = 1
        second_step = 2
        for i in range(3, n+1):
            temp = second_step
            second_step = first_step + second_step
            first_step = temp
        return second_step